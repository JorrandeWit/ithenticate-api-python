import logging
import sys
import requests
import xml.etree.ElementTree as ET

from . import Treasure
from .Exceptions import ThwartedResponseError
from .Helpers import get_xml_as_string

logger = logging.getLogger(__name__)


class Client(object):
    ENDPOINT = 'https://api.ithenticate.com/rpc'

    def __init__(self, username=None, password=None):
        if username and password:
            self.setCredentials(username, password)

        self.folders = Treasure.Folder(self)
        self.documents = Treasure.Document(self)
        self.groups = Treasure.Group(self)
        self.reports = Treasure.Report(self)

    def setCredentials(self, username, password):
        self._username = username
        self._password = password
        self._session_id = None

    def login(self):
        """
        Initiate an iThenticate session by supplying valid credentials.
        It will save the session id (sid) returned to perform further requests.
        """
        xml_string = get_xml_as_string('authentication.xml')
        xml_string = xml_string.format(
            username=self._username,
            password=self._password,
        )

        # Validation of XML
        root = ET.fromstring(xml_string)
        data = ET.tostring(root)

        try:
            xml = self.doHttpCall(data=data)
        except ThwartedResponseError as e:
            logger.warning('iThenticate login failed: {0}'.format(e.message))
            return False

        if self.getAPIStatus(xml) == 200:
            self._session_id = xml.find(".//member[name='sid']/value/string").text
            return True
        return False

    def getAPIMessages(self, xml):
        """
        Get `messages` strings coming from a general iThenticate API response.
        """
        return [node.text for node in xml.findall(".//member[name='messages']//value/string")]

    def getAPIStatus(self, xml):
        """
        Get `api_status` code coming from a general iThenticate API response.
        """
        return int(xml.find(".//member[name='api_status']/value/int").text)

    @property
    def status(self):
        return self._status if hasattr(self, '_status') else 200

    @property
    def messages(self):
        return self._latest_messages if hasattr(self, '_latest_messages') else []

    def doHttpCall(self, http_method='POST', data=None):
        """
        Make a general call to the iThenticate API.
        Response is tested for its api_status and will raise and error if the status is invalid.
        """
        try:
            headers = {
                'Content-Type': 'application/xml',
                'User-Agent': 'Python/%s' % sys.version.split(' ')[0],
            }
            response = requests.request(
                http_method,
                self.ENDPOINT,
                headers=headers,
                data=data
            )
        except Exception as e:
            raise Exception(e)

        xml = ET.fromstring(response.text)
        self._latest_messages = self.getAPIMessages(xml)
        self._status = self.getAPIStatus(xml)
        return xml

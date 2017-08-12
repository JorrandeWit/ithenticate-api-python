from ..Helpers import get_xml_as_string
from ..Object import Data


class Folder(object):
    def __init__(self, client):
        self.client = client

    def all(self):
        xml_string = get_xml_as_string('list.xml')
        xml_string = xml_string.format(sid=self.client._session_id,
                                       method_name='folder.list')

        xml_response = self.client.doHttpCall(data=xml_string)

        return Data(xml_response, 'folders',
                    self.client.getAPIStatus(xml_response),
                    self.client.getAPIMessages(xml_response))

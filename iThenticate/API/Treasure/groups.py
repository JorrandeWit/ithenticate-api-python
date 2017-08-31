from ..Helpers import get_xml_as_string
from ..Object import Data


class Group(object):
    def __init__(self, client):
        self.client = client

    def add(self, name):
        """
        Create a new folder group to your iThenticate account.

        :name: The name of the new folder group to create
        """
        assert type(name) == str

        xml_string = get_xml_as_string('add_group.xml')
        xml_string = xml_string.format(
            sid=self.client._session_id,
            name=name)

        xml_response = self.client.doHttpCall(data=xml_string)

        return Data(xml_response, 'id',
                    self.client.getAPIStatus(xml_response),
                    self.client.getAPIMessages(xml_response))

    def all(self):
        xml_string = get_xml_as_string('list.xml')
        xml_string = xml_string.format(sid=self.client._session_id,
                                       method_name='group.list')

        xml_response = self.client.doHttpCall(data=xml_string)

        return Data(xml_response, 'groups',
                    self.client.getAPIStatus(xml_response),
                    self.client.getAPIMessages(xml_response))

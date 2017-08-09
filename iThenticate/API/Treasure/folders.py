from ..Helpers import get_xml_as_string
from ..Object import List


class Folder(object):
    def __init__(self, client):
        self.client = client

    def all(self):
        xml_string = get_xml_as_string('list.xml')
        xml_string = xml_string.format(sid=self.client._session_id, method_name='folder.list')

        xml_response = self.client.doHttpCall(data=xml_string)

        return List(xml_response, 'folders', self.client.getAPIStatus(xml_response), self.client.getAPIMessages(xml_response))

    def get(self, folder_id):
        xml_string = get_xml_as_string('get.xml')
        xml_string = xml_string.format(sid=self.client._session_id,
                                       method_name='folder.get',
                                       id=folder_id)

        xml_response = self.client.doHttpCall(data=xml_string)

        return List(xml_response, 'documents', self.client.getAPIStatus(xml_response), self.client.getAPIMessages(xml_response))

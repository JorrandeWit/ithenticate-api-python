import base64

from ..Helpers import get_xml_as_string
from ..Object import List


class Document(object):
    def __init__(self, client):
        self.client = client

    def add(self, file_path, folder_id, author_first_name, author_last_name, title=None):
        encoded = base64.b64encode(open(file_path, 'rb').read())
        filename = file_path.split('/')[-1]
        title = title or filename

        xml_string = get_xml_as_string('add_document.xml')
        xml_string = xml_string.format(
            sid=self.client._session_id,
            filename=filename,
            author_last=author_last_name,
            base64=encoded,
            title=title,
            author_first=author_first_name,
            folder_id=folder_id)

        xml_response = self.client.doHttpCall(data=xml_string)

        return List(xml_response, 'uploaded', self.client.getAPIStatus(xml_response), self.client.getAPIMessages(xml_response))

    def all(self, folder_id):
        xml_string = get_xml_as_string('get.xml')
        xml_string = xml_string.format(sid=self.client._session_id,
                                       method_name='folder.get',
                                       id=folder_id)

        xml_response = self.client.doHttpCall(data=xml_string)

        return List(xml_response, 'documents', self.client.getAPIStatus(xml_response), self.client.getAPIMessages(xml_response))

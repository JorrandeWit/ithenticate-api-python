import base64

from ..Helpers import get_xml_as_string
from ..Object import Data


class Document(object):
    def __init__(self, client):
        self.client = client

    def add(self, file_path, folder_id, author_first_name, author_last_name, title=None):
        """
        Submit a new document to your iThenticate account.

        :file_path: The path to the document on your machine
        :folder_id: The folder where the document should be uploaded to
        :author_first_name: First name of first author
        :author_last_name: Last name of first author
        :title: The title of the document to use in iThenticate
        """
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

        return Data(xml_response, 'uploaded',
                    self.client.getAPIStatus(xml_response),
                    self.client.getAPIMessages(xml_response))

    def all(self, folder_id):
        """
        Retrieve all documents within a folder

        :folder_id: The folder_id to retrieve documents from.
        """
        xml_string = get_xml_as_string('get.xml')
        xml_string = xml_string.format(sid=self.client._session_id,
                                       method_name='folder.get',
                                       id=folder_id)

        xml_response = self.client.doHttpCall(data=xml_string)

        return Data(xml_response, 'documents',
                    self.client.getAPIStatus(xml_response),
                    self.client.getAPIMessages(xml_response))

    def get(self, document_id):
        """
        Retrieve the current document status information within iThenticate.

        :document_id: The document id as in iThenticate
        """
        xml_string = get_xml_as_string('get.xml')
        xml_string = xml_string.format(sid=self.client._session_id,
                                       method_name='document.get',
                                       id=document_id)

        xml_response = self.client.doHttpCall(data=xml_string)

        return Data(xml_response, 'documents',
                    self.client.getAPIStatus(xml_response),
                    self.client.getAPIMessages(xml_response))

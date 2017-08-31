from ..Helpers import get_xml_as_string
from ..Object import Data


class Report(object):
    def __init__(self, client):
        self.client = client

    def get(self, document_id):
        """
        Get the urls for the similarity report for a specific document

        :document_id: The id of the document in iThenticate
        """
        xml_string = get_xml_as_string('get.xml')
        xml_string = xml_string.format(
            sid=self.client._session_id,
            id=int(document_id))

        xml_response = self.client.doHttpCall(data=xml_string)

        return Data(xml_response, 'report_url',
                    self.client.getAPIStatus(xml_response),
                    self.client.getAPIMessages(xml_response))

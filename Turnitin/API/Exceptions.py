class ThwartedResponseError(Exception):
    def __init__(self, status_code, *args):
        super().__init__(self, status_code, *args)
        if status_code == 200:
            message = 'Successful response'
        elif status_code == 401:
            message = ('Request failed to provide an authenticated session'
                       ' id (sid) for the resource')
        elif status_code == 403:
            message = 'Access to the requested resource is not authorized'
        elif status_code == 404:
            message = 'Requested resource was not found'
        elif status_code == 500:
            message = 'Error in the request, response payload may contain errors or messages'
        else:
            message = 'Api status not known'
        self.message = message

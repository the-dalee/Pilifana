class PilightConnectionError(Exception):
    """Exception raised for errors with pilight connection.

    Attributes:
        msg      -- explanation of the error
        response -- body of the response
    """
    def __init__(self, msg):
        self.msg = msg


class PilightClientError(PilightConnectionError):
    """Exception raised for client errors with connection resulting in response with status 4xx.
       The most probable reason is the misconfiguration of the HTTP client.

    Attributes:
        msg      -- explanation of the error
        code     -- status code of the response
        response -- body of the response
    """
    def __init__(self, msg, code, response):
        self.response = response
        self.code = code
        self.msg = msg


class PilightServerError(PilightConnectionError):
    """Exception raised for server errors with connection resulting in response with status 5xx.
       The most probable reason is the misconfiguration or error behavior of the Pilight service.

    Attributes:
        msg      -- explanation of the error
        code     -- status code of the response
        response -- body of the response
    """
    def __init__(self, msg, code, response):
        self.response = response
        self.code = code
        self.msg = msg

class KairosConnectionError(Exception):
    """Exception raised for errors with KairosDB connection.

    Attributes:
        msg      -- explanation of the error
    """
    def __init__(self, msg):
        self.msg = msg


class KairosClientError(KairosConnectionError):
    """Exception raised for client errors with connection resulting in response with status 4xx.
       The most probable reason is the misconfiguration of the HTTP client.

    Attributes:
        msg      -- explanation of the error
        code     -- status code of the response
        response -- body of the response
    """
    def __init__(self, msg, code, response):
        self.response = response
        self.code = code
        self.msg = msg


class KairosServerError(KairosConnectionError):
    """Exception raised for server errors with connection resulting in response with status 5xx.
       The most probable reason is the misconfiguration or error behavior of the KairosDB.

    Attributes:
        msg      -- explanation of the error
        code     -- status code of the response
        response -- body of the response
    """
    def __init__(self, msg, code, response):
        self.response = response
        self.code = code
        self.msg = msg
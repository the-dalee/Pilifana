from http.client import HTTPConnection, HTTPSConnection
from pilifana.clients.exceptions import PilightClientError, PilightServerError, PilightConnectionError
from base64 import b64encode
import json


class PilightClient:
    def __init__(self, host, https=False, username=None, password=None):
        self.host = host
        self.https = https
        self.username = username
        self.password = password

    def __process_response(self, response):
        devices = dict()
        groups = json.loads(response)
        for group in groups:
            for device in group['devices']:
                devices[device] = group['values']
        return devices

    def get(self):
        connection = HTTPSConnection(self.host) if self.https else HTTPConnection(self.host)
        headers = dict()

        if self.username or self.password:
            credentials = "{0}:{1}".format(self.username, self.password)
            b64credentials = b64encode(credentials.encode('utf8')).decode("ascii")
            headers = {'Authorization': 'Basic {}'.format(b64credentials)}

        try:
            connection.request('GET', '/values', headers=headers)
            response = connection.getresponse()
            body = response.read().decode()
            if 400 <= response.code < 500:
                raise PilightClientError('Request rejected by pilight server', response.code, body)
            elif 500 <= response.code < 600:
                raise PilightClientError('Connection to pilight server failed', response.code, body)
            else:
                return self.__process_response(body)
        except ConnectionError as e:
            raise PilightConnectionError("Unable to connect to pilight server: " + str(e))
        finally:
            connection.close()

from http.client import HTTPConnection, HTTPSConnection
from clients.exceptions import KairosClientError, KairosServerError
import json
import time

class KairosdbClient:
    def __init__(self, host, https=False):
        self.host = host
        self.https = https

    def set(self, datapoints):
        connection = HTTPConnection(self.host) if self.https else HTTPConnection(self.host)
        try:
            body = []
            timestamp = int(time.time() * 1000)
            for key, value in datapoints.items():
                datapoint = {'name': key, 'timestamp': timestamp, 'value': value, 'tags': {'source': 'pilight'}}
                body.append(datapoint)
            connection.request('POST', '/api/v1/datapoints', json.dumps(body))
            response = connection.getresponse()
            resp_body = response.read().decode()
            if 400 <= response.code < 500:
                raise KairosClientError('Request rejected by pilight server', response.code, resp_body)
            elif 500 <= response.code < 600:
                raise KairosClientError('Connection to pilight server failed', response.code, resp_body)
            print(json.dumps(body))
        finally:
            connection.close()
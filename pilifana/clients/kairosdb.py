from http.client import HTTPConnection, HTTPSConnection
from pilifana.clients.exceptions import KairosClientError, KairosServerError, KairosConnectionError
from base64 import b64encode
import json
import time


class KairosdbClient:
    def __init__(self, host, https=False, username=None, password=None):
        self.host = host
        self.https = https
        self.username = username
        self.password = password

    def set(self, metric, datapoints):
        connection = HTTPConnection(self.host) if self.https else HTTPConnection(self.host)
        headers = dict()

        if self.username or self.password:
            credentials = "{0}:{1}".format(self.username, self.password)
            b64credentials = b64encode(credentials.encode('utf8')).decode("ascii")
            headers = {'Authorization': 'Basic {}'.format(b64credentials)}

        try:
            body = []
            timestamp = int(time.time() * 1000)
            for key, value in datapoints.items():
                datapoint = {'name': metric, 'timestamp': timestamp, 'value': value, 'tags': {'source': 'pilight', 'key': key}}
                body.append(datapoint)
            connection.request('POST', '/api/v1/datapoints', json.dumps(body), headers=headers)
            response = connection.getresponse()
            resp_body = response.read().decode()
            if 400 <= response.code < 500:
                raise KairosClientError('Request rejected by Kairos database', response.code, resp_body)
            elif 500 <= response.code < 600:
                raise KairosServerError('Connection to Kairos database failed', response.code, resp_body)

            print("Update sent")
            print(json.dumps(body))

        except ConnectionError as e:
           raise KairosConnectionError("Unable to connect to Kairos database: " + str(e))
        finally:
            connection.close()
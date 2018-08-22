import requests
from simplejson.scanner import JSONDecodeError


class SignRequests:

    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/"

    def get(self, url, payload=None):
        mac_url = self.base_url + url

        r = requests.get(mac_url, params=payload)
        try:
            result = r.json()
        except JSONDecodeError:
            result = "return JSON format error"
        return result

    def post(self, url, data=None):
        mac_url = self.base_url + url

        r = requests.post(mac_url, data=data)
        try:
            result = r.json()
        except JSONDecodeError:
            result = "return JSON format error"
        return result


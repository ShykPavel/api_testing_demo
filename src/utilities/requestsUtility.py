from src.configs.hosts_config import API_HOSTS
from requests_oauthlib import OAuth1
from src.utilities.credentialsUtility import CredentialsUtility
import requests
import os
import json


class RequestsUtility(object):

    def __init__(self):
        api_creds = CredentialsUtility.get_api_keys()
        self.env = os.environ.get("ENV", "test")
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(api_creds.get("api_key", api_creds.get("api_secret")))

    def post(self, endpoint, payload = None, headers = None, expected_status_code = 200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        url = self.base_url + endpoint
        rs_api = requests.post(url = url, data = json.dumps(payload), headers = headers, auth = self.auth)
        self.status_code = rs_api.status_code

        assert self.status_code == int(expected_status_code),\
            f"Expected status code:{expected_status_code}, actual {self.status_code}"

        return rs_api.json()

    def get(self):
        pass
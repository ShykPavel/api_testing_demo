from src.configs.hosts_config import API_HOSTS
from requests_oauthlib import OAuth1
from src.utilities.credentialsUtility import CredentialsUtility
import requests
import os
import json
import logging as logger


class RequestsUtility(object):

    def __init__(self):
        api_creds = CredentialsUtility.get_api_keys()
        self.env = os.environ.get("ENV", "test")
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(api_creds.get("api_key"), api_creds.get("api_secret"))

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, (
            f"Bad status code. "
            f"Expected: {self.expected_status_code}, "
            f"Actual: {self.status_code}, "
            f"URL: {self.url}, "
            f"Response JSON: {self.rs_json}"
        )

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if headers is None:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.post(
            url=self.url,
            data=json.dumps(payload),
            headers=headers,
            auth=self.auth
        )
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code

        self.rs_json = rs_api.json()

        self.assert_status_code()

        logger.debug(f"API POST response: {self.rs_json}")

        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if headers is None:
            headers = {"Content-Type": "application/json"}
            self.url = self.base_url + endpoint

            rs_api = requests.get(
                url=self.url,
                data=json.dumps(payload),
                headers=headers,
                auth=self.auth
            )

            self.status_code = rs_api.status_code
            self.expected_status_code = expected_status_code

            self.rs_json = rs_api.json()

            self.assert_status_code()

            logger.debug(f"API GET response: {self.rs_json}")

            return self.rs_json
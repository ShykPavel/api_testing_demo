import os

class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_api_keys():
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise Exception("The credentials 'API_KEY' and 'API_SECRET must be in env variable")
        else:
            return {"api_key" :api_key, "api_secret": api_secret}

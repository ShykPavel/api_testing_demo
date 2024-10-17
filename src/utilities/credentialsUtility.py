import os
from dotenv import load_dotenv

class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_api_keys():
        load_dotenv()

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise Exception("The credentials 'API_KEY' and 'API_SECRET must be in env variable")
        else:
            return {"api_key" :api_key, "api_secret": api_secret}

    @staticmethod
    def get_db_credentials():
        load_dotenv()

        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_socket = os.getenv("DB_SOCKET")

        if not db_user or not db_password or not db_socket:
            raise Exception("The credentials 'DB_USER', 'DB_PASSWORD' and 'DB_SOCKET' must be in env variable")
        else:
            return {"DB_USER" :db_user, "DB_PASSWORD": db_password, "DB_SOCKET": db_socket}


from src.utilities.genericUtilities import generate_random_email_and_username
from src.utilities.requestsUtility import RequestsUtility

class CustomerCreationHelper(object):
    def __init__(self):
        self.request_utility = RequestsUtility()

    def create_customer(self, email = None, username = None, expected_status_code = 201, **kwargs):
        if not email:
            email = generate_random_email_and_username().get("email")
        if not username:
            username = generate_random_email_and_username().get("username")

        payload = dict()
        payload["email"] = email
        payload["username"] = username
        payload.update(kwargs)

        create_user_json = self.request_utility.post("customers", payload = payload, expected_status_code= expected_status_code)

        return create_user_json



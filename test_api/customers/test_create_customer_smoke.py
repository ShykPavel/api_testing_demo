import pytest
import  logging as logger
from src.utilities.genericUtilities import generate_random_email_and_username
from src.helpers.customer_creation_helpers import CustomerCreationHelper

@pytest.mark.tcid29
def test_create_customer():
    logger.info("TEST: Create new customer with email and nickname")
    rand_info = generate_random_email_and_username()
    email = rand_info.get("email")
    username = rand_info.get("username")

    # make the call
    cust_obj = CustomerCreationHelper()
    cust_api_info = cust_obj.create_customer(email = email, username = username)

    # verify status code

    # verify email in the response

    # verify customer is created in db
import pytest
import logging as logger
from src.utilities.genericUtilities import generate_random_email_and_username
from src.helpers.customer_creation_helpers import CustomerCreationHelper
from src.dao.customers_dao import CustomersDAO
from src.utilities.requestsUtility import RequestsUtility

req_helper = RequestsUtility()
cust_dao = CustomersDAO()
cust_obj = CustomerCreationHelper()


@pytest.mark.customers
def test_create_customer():
    logger.info("TEST: Create new customer with email and nickname")
    rand_info = generate_random_email_and_username()
    email = rand_info.get("email")
    username = rand_info.get("username")

    cust_api_info = cust_obj.create_customer(email=email, username=username)

    assert cust_api_info["email"] == email, f"Create customer api returned wrong email. Email: {email}"
    assert cust_api_info["username"] == username, f"Create customer api returned wrong username. Username: {username}"

    cust_info = cust_dao.get_customer_by_email(email)
    cust_id_in_api = cust_api_info["id"]
    cust_id_in_db = cust_info[0]["ID"]
    assert cust_id_in_api == cust_id_in_db, f"ID's in database and api are different"


@pytest.mark.customers
def test_get_customers():
    rs_api = req_helper.get("customers")

    assert rs_api, f"List of customers is empty"

@pytest.mark.customers
def test_create_customer_fail_for_existing_email():
    existing_customer = cust_dao.get_random_user_from_db()
    existing_email = existing_customer[0]["user_email"]
    cust_api_info = cust_obj.create_customer(email=existing_email, username="username", expected_status_code=400)

    assert cust_api_info['code'] == "registration-error-email-exists", (f"Error code is incorrect for"
                                                                        f"registration with existing email")
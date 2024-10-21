import pytest
import logging as logger

from src.dao.products_dao import ProductsDAO
from src.utilities.genericUtilities import generate_random_email_and_username
from src.helpers.customer_creation_helpers import CustomerCreationHelper
from src.helpers.products_helpers import ProductsHelper
from src.dao.products_dao import ProductsDAO
from src.utilities.requestsUtility import RequestsUtility

req_helper = RequestsUtility()
products_helper = ProductsHelper()
products_dao = ProductsDAO()
cust_obj = CustomerCreationHelper()


@pytest.mark.products
def test_get_all_products():
    all_products_response = products_helper.get_all_products()
    products_api_count = len(all_products_response)

    products_db_count = len(products_dao.get_all_products())

    assert all_products_response, "List of products is empty"
    assert products_api_count == products_db_count, "Numbers of products in API and DB doesn't match"


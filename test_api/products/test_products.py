from datetime import datetime, timedelta
from random import randint

import pytest
import logging as logger

from src.dao.products_dao import ProductsDAO
from src.utilities.genericUtilities import generate_random_email_and_username
from src.helpers.customer_creation_helpers import CustomerCreationHelper
from src.helpers.products_helpers import ProductsHelper
from src.utilities.genericUtilities import generate_random_string
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

def test_get_product_by_id():
    pass
    # get a product from db

    random_product = products_dao.get_random_products_from_db(1)
    random_product_id = random_product[0]['ID']
    db_name = random_product[0]["post_title"]

    # make the call
    response_api = products_helper.get_product_by_id(random_product_id)
    api_name = response_api['name']

    # verify the response

    assert db_name == api_name, "Product names doesn't match"

def test_create_simple_product():
    payload = dict()
    payload['name'] = generate_random_string()
    payload['type'] = "simple"
    payload['regular_price'] = "12"

    product_rs = products_helper.post_new_product(payload=payload)
    assert product_rs, "Response for create a product is empty"
    assert product_rs["name"] == payload["name"], "Name from payload doesn't match response"

    product_id = product_rs["id"]
    db_product = products_dao.get_product_by_id_from_db(product_id)

    assert payload['name'] == db_product[0]['post_title'], "Name from payload doesn't match name from database"


def test_list_products_with_filter_after_x_time():

    x_days_from_today = 30
    after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
    after_created_date_iso = after_created_date.isoformat()

    payload = dict()
    payload['after'] = after_created_date_iso

    rs_api = products_helper.get_all_products(payload=payload)
    assert rs_api, "Response for get products is empty"

    db_products = products_dao.get_products_after_given_gate(after_created_date_iso)

    assert len(rs_api) == len(db_products), "Length of products doesn't match"

    ids_in_api = [i["id"] for i in rs_api]
    ids_in_db = [i["ID"] for i in db_products]

    assert  sorted(ids_in_db) == sorted(ids_in_api), "IDs in api response and database doesn't match"


def test_updating_regular_price_updates_price():

    # get random product from api
    product = products_helper.get_random_products(qty=1)
    product_id = product[0]["id"]

    payload = dict()
    payload["regular_price"] = str(randint(1,100))

    # update product price
    rs_api = products_helper.put_update_existing_product(payload=payload, product_id=product_id)

    updated_regular_price_api = rs_api["regular_price"]
    updated_price_api = rs_api["price"]

    #verify api and db changes
    assert payload["regular_price"] == updated_regular_price_api, "Regular price is not updated in API"
    assert payload["regular_price"] == updated_price_api, "Price is not updated in API"

    product_metadata_db_price = products_dao.get_product_metadata_from_db_by_key(product_id=product_id,
                                                                                 metadata_key= "_price")
    product_metadata_db_regular_price = products_dao.get_product_metadata_from_db_by_key(product_id=product_id,
                                                                                         metadata_key= "_regular_price")

    assert payload["regular_price"] == product_metadata_db_regular_price["meta_value"], "Regular price is not updated in Database"
    assert payload["regular_price"] == product_metadata_db_price["meta_value"], "Price is not updated in Database"







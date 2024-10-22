import random

from src.utilities.genericUtilities import generate_random_email_and_username
from src.utilities.requestsUtility import RequestsUtility
from src.utilities.requestsUtility import RequestsUtility


class ProductsHelper(object):
    def __init__(self):
        self.request_helper = RequestsUtility()

    def get_product_by_id(self, product_id):
        return self.request_helper.get(f"products/{product_id}")

    def get_random_products(self, qty=1):

        products = self.request_helper.get(endpoint="products")
        return random.sample(products, int(qty))


    def get_all_products(self, payload=None):
        all_products = []
        page = 1
        while True:
            req_params = {
                "per_page": 100,
                "page": page
            }
            products = self.request_helper.get(endpoint="products", payload=payload, params=req_params)

            if not products:
                break

            all_products.extend(products)

            page += 1

        return all_products

    def post_new_product(self, payload):
        return self.request_helper.post("products", payload=payload, expected_status_code=201)

    def put_update_existing_product(self, payload, product_id):
        return self.request_helper.put(f"products/{product_id}", payload=payload)







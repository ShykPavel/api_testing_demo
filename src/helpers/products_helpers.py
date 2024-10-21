from src.utilities.genericUtilities import generate_random_email_and_username
from src.utilities.requestsUtility import RequestsUtility
from src.utilities.requestsUtility import RequestsUtility


class ProductsHelper(object):
    def __init__(self):
        self.request_helper = RequestsUtility()
    
    def get_all_products(self):
        all_products = []
        page = 1
        while True:
            req_params = {
                "per_page": 100,
                "page": page
            }
            products = self.request_helper.get(endpoint="products", params=req_params)

            if not products:
                break

            all_products.extend(products)

            page += 1

        return all_products



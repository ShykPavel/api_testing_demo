from src.utilities.db_utility import DBUtility
import random

class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_all_products(self):
        sql = "SELECT * FROM local.wp_posts WHERE post_type = 'product'"
        response_sql = self.db_helper.execute_select(sql)

        return response_sql

    def get_random_products_from_db(self, qty=1):

        sql = "SELECT * FROM local.wp_posts WHERE post_type = 'product' ORDER BY id DESC LIMIT 5000;"

        response_sql = self.db_helper.execute_select(sql)

        return random.sample(response_sql, int(qty))


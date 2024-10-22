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


    def get_product_by_id_from_db(self, product_id):
        sql = f"SELECT * FROM local.wp_posts WHERE ID = {product_id}"
        response_sql = self.db_helper.execute_select(sql)

        return response_sql

    def get_product_metadata_from_db_by_key(self, product_id, metadata_key=None):
        sql = f"SELECT * FROM local.wp_postmeta where post_id = {product_id}"
        response_sql = self.db_helper.execute_select(sql)

        if metadata_key:
            for key in response_sql:
                if key["meta_key"] == metadata_key:
                    return key
        else:
            return response_sql


    def get_products_after_given_gate(self, date_iso):

        sql = f"SELECT * FROM local.wp_posts WHERE post_type = 'product' AND post_date > '{date_iso}' LIMIT 5000;"
        response_sql = self.db_helper.execute_select(sql)

        return response_sql
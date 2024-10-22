from src.utilities.db_utility import DBUtility
import random

class CouponsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_all_coupons(self):
        sql = "SELECT * FROM local.wp_posts WHERE post_type = 'shop_coupon'"
        response_sql = self.db_helper.execute_select(sql)

        return response_sql

    def get_random_coupon_from_db(self, qty=1):

        sql = "SELECT * FROM local.wp_posts WHERE post_type = 'shop_coupon' ORDER BY id DESC LIMIT 5000;"

        response_sql = self.db_helper.execute_select(sql)

        return random.sample(response_sql, int(qty))


    def get_coupon_by_id_from_db(self, coupon_id):
        sql = f"SELECT * FROM local.wp_posts WHERE ID = {coupon_id}"
        response_sql = self.db_helper.execute_select(sql)

        return response_sql

    def get_coupon_metadata_from_db_by_key(self, coupon_id, metadata_key=None):
        sql = f"SELECT * FROM local.wp_postmeta where post_id = {coupon_id}"
        response_sql = self.db_helper.execute_select(sql)

        if metadata_key:
            for key in response_sql:
                if key["meta_key"] == metadata_key:
                    return key
        else:
            return response_sql


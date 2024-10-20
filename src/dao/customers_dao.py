from src.utilities.db_utility import DBUtility
import random

class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}'"
        response_sql = self.db_helper.execute_select(sql)

        return response_sql

    def get_random_user_from_db(self, qty=1):

        sql = "SELECT * FROM local.wp_users ORDER BY id DESC LIMIT 5000;"

        response_sql = self.db_helper.execute_select(sql)

        return random.sample(response_sql, int(qty))


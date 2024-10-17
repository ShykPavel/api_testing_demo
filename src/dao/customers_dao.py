from src.utilities.db_utility import DBUtility

class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}'"
        response_sql = self.db_helper.execute_sql(sql)

        print(response_sql)
        print("bp")

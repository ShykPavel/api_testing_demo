import pymysql.cursors
import logging as logger
from src.utilities.credentialsUtility import CredentialsUtility

class DBUtility(object):

    def __init__(self):
        credentials_helper = CredentialsUtility()
        self.credentials = credentials_helper.get_db_credentials()
        self.host = "localhost"


    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.credentials.get('DB_USER'),
                                     password=self.credentials.get('DB_PASSWORD'),
                                     unix_socket=self.credentials.get('DB_SOCKET'))

        return connection

    def execute_select(self, sql):
        connection = self.create_connection()

        try:
            logger.debug(f"Executing {sql}")
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            results_dict =  cursor.fetchall()
            cursor.close()
        except Exception:
            raise Exception(f"Failed running SQL: {sql}. Error: {str(Exception)}")
        finally:
            connection.close()

        return results_dict
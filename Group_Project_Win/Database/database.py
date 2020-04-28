import psycopg2 as psql


class Database:
    def __init__(self, app_db_name, user, password, host, port):
        try:
            self.connection = psql.connect(
                database=app_db_name,
                user=user,
                password=password,
                host=host,
                port=port)

            #self.send_query("""
            #CREATE DATABASE %s
            #""" % app_db_name)
        except psql.OperationalError as error:
            raise error

    def send_query(self, query):
        self.connection.autocommit = True
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
        except psql.OperationalError as error:
            raise error

    def send_read_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except psql.OperationalError as error:
            raise error
import sqlite3
from Lesson_25.db_queries import DbQueries as query


class BaseDbMethods:

    @staticmethod
    def connect_or_create_sqlite_db():
        connection = sqlite3.connect("Dima_test_db.db")
        return connection

    @staticmethod
    def execute_query_and_return_data(connection, query: str):
        cursor = connection.cursor()
        cursor = cursor.execute(query)
        cursor = cursor.fetchall()
        return cursor

    @staticmethod
    def close_db(connection):
        connection.close()


class DB(BaseDbMethods):

    def create_new_tables_in_db(self, connection):
        try:
            self.execute_query_and_return_data(connection, query.CREATE_TABLE_DATA.value)
            self.execute_query_and_return_data(connection, query.CREATE_TABLE_VENDORS.value)
            self.execute_query_and_return_data(connection, query.CREATE_TABLE_CUSTOMERS.value)
        except sqlite3.OperationalError:
            pass

    def add_data_to_the_tables(self, connection):
        self.insert_data_into_table(connection, query.INSERT_INTO_CUSTOMERS.value)
        self.insert_data_into_table(connection, query.INSERT_INTO_DATA.value)
        self.insert_data_into_table(connection, query.INSERT_INTO_VENDORS.value)

    def insert_data_into_table(self, connection, list_or_queries: list):
        for _ in list_or_queries:
            self.execute_query_and_return_data(connection, _)

import pytest
from Lesson_25.basedbmethods import DB


@pytest.fixture
def prepare_data():
    db = DB()
    connection = db.connect_or_create_sqlite_db()
    db.create_new_tables_in_db(connection)
    db.add_data_to_the_tables(connection)
    yield connection
    db.close_db(connection)

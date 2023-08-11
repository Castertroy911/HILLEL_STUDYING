from Lesson_25.basedbmethods import DB


class TestDataFromDb:

    def test_data_from_customers_table(self, prepare_data):
        db = DB()
        result = db.execute_query_and_return_data(prepare_data, "SELECT * FROM Customers")
        assert "Johnny" in result[0], "Johnny not in the table"

    def test_data_from_vendors_table(self, prepare_data):
        db = DB()
        result = db.execute_query_and_return_data(prepare_data, "SELECT * FROM Vendors")
        assert "Olaf" in result[0], "Olaf not in the table"

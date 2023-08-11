from enum import Enum


class DbQueries(Enum):
    CREATE_TABLE_DATA = "CREATE TABLE Data(data_id INTEGER PRIMARY KEY, name TEXT, data INTEGER CHECK(data<10));"
    INSERT_INTO_DATA = ["INSERT INTO Data(name, data) VALUES ('Hello', 3);"]
    CREATE_TABLE_VENDORS = "CREATE TABLE Vendors(vendor_id INTEGER PRIMARY KEY, " \
                           "name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL);"
    CREATE_TABLE_CUSTOMERS = "CREATE TABLE Customers(customer_id INTEGER PRIMARY KEY, name TEXT NOT NULL, " \
                             "vendor_name TEXT, deal INTEGER, money REAL);"
    INSERT_INTO_CUSTOMERS = ["INSERT INTO Customers(name, vendor_name, deal, money) VALUES ('Johnny', 'Johny', 3, "
                             "324234.4);", "INSERT INTO Customers(name, money) VALUES ('Andrew', 324234.4);"]
    INSERT_INTO_VENDORS = ["INSERT INTO Vendors(name, item, deal, price) VALUES ('Olaf', 'Car', 3, 14.4);",
                           "INSERT INTO Vendors(name, item, deal, price) VALUES ('John', 'Train', 3, 14.4), "
                           "('Jerom', 'Tram', 1, 2.4), ('Anna', 'Plane', 7, 100), ('Igor', 'Helicopter', 11, 1200);",
                           "INSERT INTO Vendors(name, deal, price) VALUES ('Joseph', 7, 14.4), ('Albert', 111, 0);"]

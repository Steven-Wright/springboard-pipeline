from etl.DatabaseUtils import DatabaseUtils
import mysql.connector

class MySQLUtils(DatabaseUtils):
    def __init__(self, username, password, database):
        self.__connection = mysql.connector.connect(
            user=username,
            password=password,
            database=database)
        self.__cursor = None
        self.__dirty = None

    def __enter__(self):
        self.__cursor = self.__connection.cursor()
        self.__dirty = False
        return self

    def __exit__(self, type, val, traceback):
        self.__cursor.close()
        self.__cursor = None
        
        if self.__dirty:
            self.__connection.commit()
        self.__dirty = None

    def select_popular_tickets(self):
        if self.__cursor is None:
            raise RuntimeError("MySQLUtils must be used as context manager")

        query=("SELECT event_name, event_city "
               "FROM ticket_sales "
               "ORDER BY num_tickets "
               "LIMIT 3")
        self.__cursor.execute(query)
        return self.__cursor.fetchall()
        
    def insert_ticket_sales(self, record):      
        if self.__cursor is None:
            raise RuntimeError("MySQLUtils must be used as context manager")

        query = ("INSERT INTO ticket_sales(ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        self.__cursor.execute(query, tuple(record))
        self.__dirty = True
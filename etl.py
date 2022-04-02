import mysql.connector
import logging
import csv
import argparse

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            user='steven',
            password='springboard',
            database='ticketing',
        )
    except Exception as error:
        logging.exception("Error connecting to ticketing system database")

    return connection

def load_csv(connection, csv_path):
    cursor = connection.cursor()

    try:
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file, 
        fieldnames=["ticket_id",
            "trans_date",
            "event_id",
            "event_name",
            "event_date",
            "event_type",
            "event_city",
            "customer_id",
            "price",
            "num_tickets"])

            insert_query = ("INSERT INTO ticket_sales(ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets)"
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            for row in reader:
                cursor.execute(insert_query, tuple(row.values()))
            
            connection.commit()

    except FileNotFoundError:
        logging.exception("Could not find file at %s", csv_path)
    
    except mysql.connector.errors.DatabaseError:
        logging.exception("Error executing query")

    finally:
        cursor.close()        

def query_popular_tickets(connection):
    
    query=("SELECT event_name, event_city "
           "FROM ticket_sales "
           "ORDER BY num_tickets "
           "LIMIT 3")
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    return records

# Setup command line interface
parser = argparse.ArgumentParser()
parser.description = "Interact with the ticketing system database, now through python :)"
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-f", "--file",)
group.add_argument("-l", "--list", action="store_true")

args=parser.parse_args()
conn = get_db_connection()

if args.list:
    records = query_popular_tickets(conn)
    if len(records) > 0:
        print("Here are the most popular tickets:")
        for record in records:
            print("- {0}, {1}".format(record[0], record[1]))
    else:
        print("There are no ticket sales in the database.")

if args.file is not None:
    load_csv(conn, args.file)
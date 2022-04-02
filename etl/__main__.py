from etl import CSVRecordProvider
from etl import MySQLUtils
import argparse
import logging

# Setup command line interface
parser = argparse.ArgumentParser()
parser.description = "Interact with the ticketing system database, now through python :)"
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-f", "--file",)
group.add_argument("-l", "--list", action="store_true")

args=parser.parse_args()

# Main entry point
if args.list:
    # --list option
    with MySQLUtils("steven", "springboard", "ticketing") as db:
        records = db.select_popular_tickets()
    
    if len(records) > 0:
        print("Here are the most popular tickets:")
        for record in records:
            print("- {0}, {1}".format(record[0], record[1]))
    else:
        print("There are no ticket sales in the database.")

if args.file is not None:
    # --file option
    try:
        with CSVRecordProvider(args.file) as records:
                with MySQLUtils("steven", "springboard", "ticketing") as db:
                    for record in records:
                        db.insert_ticket_sales(record)
    except FileNotFoundError:
        logging.exception("Could not find file at %s", args.file)
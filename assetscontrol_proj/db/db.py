import sqlite3
from sqlite3 import Error
from app.properties import Properties
import sys
import os

def drop_db():
    
    props = Properties().read_properties()
    db_file = props["database.name"]

    """ delete the database file """
    try:
        if os.path.exists(db_file):
            os.remove(db_file)
            print(f"Database {db_file} deleted successfully.")
        else:
            print(f"Database {db_file} does not exist.")
    except Error as e:
        print(e)            
            
def create_db():
    
    props = Properties().read_properties()
    db_file = props["database.name"]

    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            print("Connection closed.")
            
def create_tables():

    props = Properties().read_properties()
    db_file = props["database.name"]
    db_ddl_location = props["database.ddl.location"]

    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
        with open(f'{db_ddl_location}/create_tables.sql') as f:
            conn.executescript(f.read())
        print("Tables created successfully.")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            print("Connection closed.")

def drop_tables():
    
    props = Properties().read_properties()
    db_file = props["database.name"]
    db_ddl_location = props["database.ddl.location"]

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
        with open(f'{db_ddl_location}/drop_tables.sql') as f:
            conn.executescript(f.read())
        print("Tables dropped successfully.")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            print("Connection closed.")
            
if len(sys.argv) < 2:
    print("Usage: python db.py <command>")
    print("Commands: create_db, create_tables, drop_tables, drop_db")
    sys.exit(1)

if __name__ == "__main__":
    if sys.argv[1] == "create_db":
        create_db()
    elif sys.argv[1] == "create_tables":
        create_tables()
    elif sys.argv[1] == "drop_tables":
        drop_tables()
    elif sys.argv[1] == "drop_db":
        drop_db()
    else:
        print(f'DB Command Not Recognized {sys.argv[1]}. Please use create_db, create_tables, drop_tables, or drop_db.')
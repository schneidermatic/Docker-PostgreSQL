#!/usr/bin/env python3

import psycopg2
from psycopg2 import sql
import requests
import sys

# URL to the GitHub repository containing the SQL files
GITHUB_URL = "https://raw.githubusercontent.com/yugabyte/yugabyte-db/refs/heads/master/sample/"
# Local path to save the downloaded SQL files
LOCAL_PATH = "../data/"
# Dictionary containing the URLs and local paths for the DDL and data SQL files
DB_FILES = {
    "DDL": {"URL": GITHUB_URL + "northwind_ddl.sql", "LOCAL": LOCAL_PATH + "northwind_ddl.sql"},
    "DATA": {"URL": GITHUB_URL + "northwind_data.sql", "LOCAL": LOCAL_PATH + "northwind_data.sql"},
}

def download_file(url, local_filename):
    """
    Downloads a file from the given URL and saves it to the local filename.
    """
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Downloaded {local_filename} from {url}")
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")

def get_cursor(db_name):
    """
    Connects to the PostgreSQL database and returns a cursor.
    """
    try:
        conn = psycopg2.connect(f"host='localhost' dbname='{db_name}' user='postgres' password='changeme'")
        conn.autocommit = True
        return conn.cursor()
    except psycopg2.Error as e:
        print(e)
        return None

def execute_sql_file(cursor, file_path):
    """
    Executes the SQL commands in the given file using the provided cursor.
    """
    try:
        print(f"Executing SQL commands from {file_path}")
        with open(file_path, "r") as file:
            cursor.execute(file.read())
    except psycopg2.Error as e:
        print(e)

def create_database():
    """
    Creates the 'northwind' database.
    """
    cursor = get_cursor("postgres")
    if cursor:
        try:
            cursor.execute(sql.SQL('CREATE DATABASE {};').format(sql.Identifier("northwind")))
        except psycopg2.Error as e:
            print(e)
        finally:
            cursor.close()

def main():
    """
    Main function to download SQL files, create the database, and execute the SQL files.
    """
    for value in DB_FILES.values():
        download_file(value['URL'], value['LOCAL'])
    create_database()
    cursor = get_cursor("northwind")
    if cursor:
        execute_sql_file(cursor, DB_FILES["DDL"]["LOCAL"])
        execute_sql_file(cursor, DB_FILES["DATA"]["LOCAL"])
        cursor.close()

if __name__ == "__main__":
    sys.exit(main())

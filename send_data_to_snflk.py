import snowflake.connector
import os
from dotenv import load_dotenv
load_dotenv()
import getdata.getdata
from os.path import join, dirname
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PASSWORD = os.environ.get('PASSWORD')
USER=os.environ.get('USER')
ACCOUNT=os.environ.get('ACCOUNTS')
WAREHOUSE=os.environ.get('WAREHOUSE')
DATABASE=os.environ.get('DATABASE')
SCHEMA=os.environ.get('SCHEMA')

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
    )

conn.cursor().execute(
    "CREATE OR REPLACE TABLE "
    "test_table(col1 integer, col2 string)")

conn.cursor().execute(
    "INSERT INTO test_table(col1, col2) VALUES " + 
    "    (123, 'test string1'), " + 
    "    (456, 'test string2')")
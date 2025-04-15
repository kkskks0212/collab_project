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
ACCOUNT=os.environ.get('ACCOUNT')
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


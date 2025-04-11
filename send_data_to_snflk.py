import snowflake
import os
import dotenv

PASSWORD = os.getenv('PASSWORD')
USER=os.getenv('USER')
ACCOUNT=os.getenv('ACCOUNT')
WAREHOUSE=os.getenv('WAREHOUSE')
DATABASE=os.getenv('DATABASE')
SCHEMA=os.getenv('SCHEMA')

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
    )
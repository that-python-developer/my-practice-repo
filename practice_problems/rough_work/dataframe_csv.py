import time
import mariadb
import psycopg2
import pandas as pd


from sqlalchemy import create_engine
from datetime import timedelta, date, datetime
from dateutil.relativedelta import relativedelta

postgreclock_2 = datetime.now()
print(postgreclock_2)
start_time = datetime(2022, 5, 22, 11, 58, 0)  # start_time
end_time = datetime(2022, 5, 28, 2, 0, 0)  # end_time

# Maria DB Table
fk_instance_id = 31
schema_name = 'dmart_mis'
table_name = 'transaction_process'

# Postgres Table
schema_name2 = 'edw_tab'
table_name2 = 'tmp_stg_sale_line_dmart'

# Enter connection details - Mariadb
hostname1 = '124.153.107.29'
portnumber1 = 55433  # 3306 Maria DB & 5432 for PostGreSQL
databasename1 = 'pentaho'
user1 = 'pentaho'
pass1 = 'pentaho'

# Enter connection details - Postgres
hostname2 = '172.25.185.16'
portnumber2 = 5432  # 3306 Maria DB & 5432 for PostGreSQL
databasename2 = 'edw_prod'
user2 = 'pentaho'
pass2 = 'pentaho'
# ---------------------------------------------------------------------------------------------


def dbdata(database_name, query_):
    if database_name == "maria":
        # establishing the connection
        connection = mariadb.connect(
           database=databasename1, user=user1 , password=pass1, host= hostname1, port= portnumber1)
    elif database_name == "postgre":
        # establishing the PostgreSQL connection
        connection = psycopg2.connect(
           database=databasename2, user=user2 , password=pass2, host= hostname2, port= portnumber2)
    # Creating a cursor object using the cursor() method
    cur = connection.cursor()
    cur.execute(query_)
    data = cur.fetchall()
    # Fetching Column headers seperately and inserting into Table
    column_names = [desc[0] for desc in cur.description]
    data.insert(0, column_names)
    # Converting the list to Data Frame
    dbdatadf = pd.DataFrame(data)
    # Using First row as Column Header
    new_header = dbdatadf.iloc[0]
    dbdatadf = dbdatadf[1:]
    dbdatadf.columns = new_header
    connection.close()
    return dbdatadf
# ---------------------------------------------------------------------------------------------


select_ = "SELECT * FROM " + schema_name + "." + table_name
where_clause_ = " where date_entry between '" + str(start_time) + "' and '" + str(end_time) + "' LIMIT 10;"
query_ = select_ + where_clause_
deltadata = dbdata("maria",query_)
deltadata['fk_instance_id'] = fk_instance_id
count_source_rows = deltadata.shape[0]
print("Source prim_id Count "+str(count_source_rows))
# Target DB
conn_string = 'postgresql://pentaho:pentaho@172.25.185.16/edw_prod'
# perform to_sql
dbconnection = create_engine(conn_string)
pgengine = dbconnection.connect()
postgreclock_1 = datetime.now()
print(str(postgreclock_1)+' Pushing to PostgreSQL table')
deltadata.to_sql(table_name2, con=pgengine, schema=schema_name2, if_exists='replace',  index=False)
postgreclock_2 = datetime.now()
print(str(postgreclock_2)+' Success Pushed to PostgreSQL table in ' + str(postgreclock_2 - postgreclock_1) )
pgengine.close()
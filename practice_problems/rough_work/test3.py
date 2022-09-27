import os
import csv
from pandas import read_sql

from sqlalchemy import create_engine  # for creating engine to connect
from os.path import join as path_join
from datetime import datetime

python_process_name = 'stg_sale_line_load'
start_time = datetime.now()

# Source Connection Details
host_name = '172.25.146.20'
port_number = 3306
database_name = 'pentaho'
user_name = 'pentaho'
password = 'pentaho'

source_conn_string = f"mysql://{user_name}:{password}@{host_name}:{port_number}/{database_name}"

# Establish Connection With Source
db_connection = create_engine(source_conn_string)
pgengine = db_connection.connect()
conn = pgengine.connect()

# Source Table Details
instance_id = 16
schema_name = 'relinace_mis'
table_name = 'transaction_process'

# Target Tables in PostgreSQL
db_name = 'edw_dev'
# db_name = 'edw_prod'
db_host = '172.25.146.20'
# db_host = '172.25.185.16'

# File path
# csv_file_path = 'D:/test/sample.csv'

query = f"""
    SELECT *
    FROM {schema_name}.{table_name}
    LIMIT 10
"""
result_df = read_sql(query, conn)
print(result_df)

# with open(r'{}'.format(csv_file_path), 'a', encoding='utf-8') as csv_file:
#     csv_writer = csv.writer(csv_file, lineterminator='\n')  # use line terminator for windows
#     if os.stat(csv_file_path).st_size == 0:
#         column_names = cursor._metadata.keys
#         csv_writer.writerow(column_names)
#     csv_writer.writerows(cursor)

conn.close()

end_time = datetime.now()
delta = end_time - start_time

print('success!')

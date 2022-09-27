from sqlalchemy import create_engine #for creating engine to connect
import pandas as pd #for dataframe
import datetime #for current timestamps

start_time = datetime.datetime.now() # start process logs
python_process_name = 'auto_vacuum'

##Target Tables in PostgreSQL
target_schema = 'edw_tab'
target_table = ''

# dbname = 'edw_dev'
dbname = 'edw_prod'
# dbhost = '172.25.146.20'
dbhost = '172.25.185.16'

##Accessing the target Database
conn_string = 'postgresql://pentaho:pentaho@'+ dbhost + '/' + dbname

##Establish Authorisation with the connection string and create pointer as pgengine
dbconnection = create_engine(conn_string, isolation_level='AUTOCOMMIT')
pgengine = dbconnection.connect()

conn = pgengine.connect()

get_dead_tuples = """
    select
        schemaname as schema_name,
        pg_stat_user_tables.relname as table_name
    FROM
       pg_stat_user_tables INNER JOIN pg_class ON pg_stat_user_tables.relname = pg_class.relname
       where schemaname ='{target_schema}'
       and n_dead_tup >100
    ORDER by n_dead_tup desc;
""".format(target_schema=target_schema)
dead_tuples_df = pd.read_sql(get_dead_tuples, conn)

# Vacuum Query
for i, row in dead_tuples_df.iterrows():
    vacuum_query = 'VACUUM FULL {}.{};'.format(row['schema_name'], row['table_name'])
    conn.execute(vacuum_query)

end_time = datetime.datetime.now()
delta = end_time - start_time

log_update = f"""
INSERT INTO edw_tab.admin_etl_history_python 
(python_process_name,schema_name,table_name,records_count,start_time,end_time,execution_time) 
VALUES
('{python_process_name}','{target_schema}','{target_table}','{count_rows1}','{start_time}','{end_time}','{delta}');
"""
conn.execute(log_update)
print('Log Update - Success!')

conn.close()

print('success!')
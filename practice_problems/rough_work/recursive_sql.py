import time
import psycopg2

from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta, date

from pandas import read_sql
from sqlalchemy import create_engine


user1 = 'pentaho'  # input('Username:')
pass1 = 'pentaho'  # input('Password:')
# db_name = 'edw_dev'
# db_host = '124.153.107.29'
# db_port = '55432'
db_name = 'edw_prod'
db_host = '172.25.185.16'
db_port = '5432'

# establishing the connection
# connection = psycopg2.connect(
#     database=dbname,
#     user=user1,
#     password=pass1,
#     host=db_host,
#     port=db_port
# )
conn_string = f'postgresql://{user1}:{pass1}@{db_host}:{db_port}/{db_name}'
db_connection = create_engine(conn_string)
pgengine = db_connection.connect()

print('Connection to Development - Successful')
# Creating a cursor object using the cursor() method

# cur = connection.cursor()
get_person_codes = """
    SELECT
        distinct on (person_code) person_code as filter_person_code, 
        person_name as filter_person_name
    FROM edw_tab.dw_dim_person ddp 
"""
person_codes = read_sql(get_person_codes, pgengine)
for i, row in person_codes.iterrows():
    insert_query = """
        -- This will give you the self data as employee and manager
        select 
            '{filter_person_code}' as filter_person_code,
            '{filter_person_name}' as filter_person_name,
            e.person_code,
            e.person_name,
            e.joining_date,
            e.dept_code,
            e.designation_code,
            e.role_code,
            e.city,
            e.state,
            e.active,
            0 as level
        from edw_tab.dw_dim_person e
        join edw_tab.dw_dim_person m on e.person_code = m.person_code
        where e.person_code = '{filter_person_code}'
        union all
        -- This will give you the subordinates data recursively
        select *
        from (
            WITH RECURSIVE subordinate AS (
                SELECT  
                    person_code,
                    person_name,
                    joining_date,
                    dept_code,
                    designation_code,
                    role_code,
                    city,
                    state,
                    active,
                    manager_code,
                    0 AS level
                FROM edw_tab.dw_dim_person		
                where person_code = '{filter_person_code}'
                UNION ALL
                SELECT  
                    e.person_code,
                    e.person_name,
                    e.joining_date,
                    e.dept_code,
                    e.designation_code,
                    e.role_code,
                    e.city,
                    e.state,
                    e.active,
                    e.manager_code,
                    level + 1
                FROM edw_tab.dw_dim_person e
                JOIN subordinate s
                ON e.manager_code = s.person_code
            ) 
            SELECT 
                '{filter_person_code}' as filter_person_code,
                '{filter_person_name}' as filter_person_name,
                s.person_code,
                s.person_name,
                s.joining_date,
                s.dept_code,
                s.designation_code,
                s.role_code,
                s.city,
                s.state,
                s.active,
                s.level
            FROM subordinate s
            JOIN edw_tab.dw_dim_person m
            ON s.manager_code = m.person_code 
            where s.level <> 0
            ORDER BY level
        ) foo
    """.format(
        filter_person_code=row['filter_person_code'],
        filter_person_name=row['filter_person_name']
    )
    insert_df = read_sql(insert_query, pgengine)
    insert_df.to_sql(
        'dw_dim_person_manager',
        con=pgengine.execution_options(autocommit=True),
        schema='edw_tab', index=False, if_exists='append', method='multi'
    )
print("------------------------------------------------ Task Completed -----------------------------------------------")

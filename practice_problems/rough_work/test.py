# import os
# import csv
#
# from sqlalchemy import create_engine  # for creating engine to connect
# from os.path import join as path_join
#
# # Target Tables in PostgreSQL
# db_name = 'edw_dev'
# # db_name = 'edw_prod'
# db_host = '172.25.146.20'
# # db_host = '172.25.185.16'
#
# # File path
# csv_file_path = 'D:/test/sample.csv'
#
# # Accessing the target Database
# conn_string = 'postgresql://pentaho:pentaho@' + db_host + '/' + db_name
#
# # Establish Authorisation with the connection string and create pointer as pgengine
# db_connection = create_engine(conn_string)
# pgengine = db_connection.connect()
#
# conn = pgengine.connect()
#
# query = """
#     SELECT *
#     FROM edw_dim.dw_dim_store
#     LIMIT 10
# """
# cursor = conn.execute(query)
# with open(r'{}'.format(csv_file_path), 'a', encoding='utf-8') as csv_file:
#     csv_writer = csv.writer(csv_file, lineterminator='\n')  # use line terminator for windows
#     if os.stat(csv_file_path).st_size == 0:
#         column_names = cursor._metadata.keys
#         csv_writer.writerow(column_names)
#     csv_writer.writerows(cursor)

from itertools import chain, combinations

# arr = sorted([1, 2, 3, 7, 5])
# for i in range(0, len(arr)):
# combos = [print(x) for x in chain.from_iterable(combinations(arr, r) for r in range(len(arr)+1)) if sum(x) == 12]
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = [1, 2, 3, 7, 5]
s = 12
n = 5
# for i in range(0, n):
#     for j in range(i, n+1):
#         if sum(arr[i:j]) == s:
#             print(arr[i:j], i+1, j)

for i in range(0, n):
    for j in range(i, n+1):
        if sum(arr[i:j]) == s:
            print(i+1, j)
        # if sum(arr[i:j]) == s:
        #     print(i,j)

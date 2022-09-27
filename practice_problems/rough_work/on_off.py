from pandas import read_sql, DataFrame
from sqlalchemy import create_engine
from datetime import datetime

# Target Tables in PostgreSQL
db_name = 'edw_dev'
# db_name = 'edw_prod'
db_host = '172.25.146.20'
# db_host = '172.25.185.16'

# Accessing the target Database
conn_string = 'postgresql://pentaho:pentaho@' + db_host + '/' + db_name

# Establish Authorisation with the connection string and create pointer as pgengine
db_connection = create_engine(conn_string)
pgengine = db_connection.connect()

conn = pgengine.connect()

query = f"""
    select  *
    from edw_adhoc.event_status
"""
result_df = read_sql(query, conn)
t = {}
i = 0
prev_step = 'off'
df = DataFrame(columns=['login', 'logout', 'on_count'])
for k, row in result_df.iterrows():
    if row['status'] == 'on':
        if prev_step == 'on':
            t[i].append(row['event_time'])
        else:
            t[i] = [row['event_time']]
        prev_step = 'on'
    if row['status'] == 'off':
        t[i].append(row['event_time'])
        prev_step = 'off'
        df = df.append(
            {
                'login': t[i][0],
                'logout': t[i][-1],
                'on_count': len(t[i])-1
            },
            ignore_index=True
        )
        i += 1
print(df)
conn.close()



# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         for i, e in reversed(list(enumerate(digits))):
#             if digits[i] == 9:
#                 digits = self.add_one(digits, i)
#                 if digits[0] == 0:
#                     digits.insert(0, 1)
#             else:
#                 digits[i] += 1
#                 return digits
#
#         return digits
#
#     def add_one(self, digits, index):
#         if digits[index] == 9:
#             digits[index] = 0
#         else:
#             digits[index] += 1
#         return digits
#
#
# if __name__ == '__main__':
#     s = Solution()
#     print(s.plusOne([1, 9, 9]))
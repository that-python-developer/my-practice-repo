# query = """
#     select
#     a.utid as utid,
#     b.store_code,
#     (select max(date_fld) as date_fld from edw_tab.dim_Date where last_x_day={day}) as timefilter,
#     sum(a.sale_net_val) as sale_net_val,
#     sum(dcc_trx_val) as dcc_trx_val,
#     sum(sale_trx_val) as sale_trx_val,
#     sum(sale_emi_val) as sale_emi_val
#     FROM edw_tab.agg_dly_utid_sales a
#     JOIN edw_tab.dim_date d ON a.date_key = d.date_key
#     join edw_Tab.tab_utid_hierarchy_view_all b on a.utid =b.utid
#     WHERE store_category not IN('DELETE') and general_purpose_utid ='NO'
#     and d.date_key
#         between (select (date_fld - interval '29' day)::date from edw_tab.dim_Date where last_x_day={day})
#         and ( select date_key from edw_tab.dim_Date where last_x_day={day})
#     and last_x_month =1
#     group by a.utid ,b.store_code
# """
#
# t = '\nUNION ALL\n'.join(
#                 [
#                     query.format(
#                         day=day
#                     ) for day in range(1, 32)
#                 ]
#             )
# # print(t)
#
# load_data = f"""
#     \\COPY FROM '' DELIMITER ',' CSV HEADER;
# """
# print(load_data)



from datetime import datetime, date
from dateutil.relativedelta import relativedelta

start_time = str(date.today() - relativedelta(days=1)) + ' 00:00:00'
start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
end_time = str(date.today()) + ' 00:00:00'
end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

print(start_date)
print(end_date)
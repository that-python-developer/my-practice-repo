import time
from dateutil.relativedelta import relativedelta
import pandas as pd
import psycopg2
from datetime import datetime as dt
from datetime import timedelta, date
from sqlalchemy import create_engine #for creating engine to connect
import datetime
import psycopg2
import pandas as pd
import datetime


start_date = date(2022, 2, 6)
end_date = date(2022, 2, 10)
number_of_days = end_date - start_date

user1 = 'pentaho'#input('Username:')
pass1 = 'pentaho'#input('Password:')
dbname = 'edw_dev'
dbhost = '172.25.146.20'
# dbname = 'edw_prod'
# dbhost = '172.25.185.16'
dbport = '5432'

#establishing the connection
connectn = psycopg2.connect(database=dbname, user=user1 , password=pass1, host=dbhost, port= dbport )
print('Connection to Development - Successful')
#Creating a cursor object using the cursor() method

for i in range(number_of_days.days + 1):
    for_date = start_date + timedelta(days=i)
    cur = connectn.cursor()
    query = """
    insert into edw_tab.agg_dly_utid_transactions (
        date_key,
        utid,
        category_name,
        brand,
        model,
        issuer_bank,
        tenure_type,
        service_type,
        credit_debit,
        product_type,
        sale_product_invc_count,
        sale_trx_invc_count,
        sale_trx_val_excluding_test_transactions_invc_count,
        sale_net_invc_count,
        sale_loan_invc_count,
        sale_emi_invc_count,
        sale_nocostemi_invc_count,
        sale_genie_disc_invc_count,
        sale_cashback_disc_invc_count,
        sale_eft_invc_count,
        bank_emi_invc_count,
        brand_emi_invc_count,
        exclusive_emi_invc_count,
        wallet_emi_invc_count,
        dc_emi_invc_count,
        instant_discount_invc_count,
        additional_cashback_invc_count,
        dcc_trx_count,
        genie_coupon_count,
        sale_product_val,
        sale_trx_val,
        sale_trx_val_excluding_test_transactions,
        sale_net_val,
        sale_loan_val,
        sale_emi_val,
        sale_nocostemi_val,
        sale_genie_disc_val,
        sale_cashback_disc_val,
        emi_amount,
        sale_eft_val,
        bank_emi_val,
        brand_emi_val,
        exclusive_emi_val,
        wallet_emi_val,
        dc_emi_val,
        instant_discount,
        additional_cashback,
        dcc_trx_val,
        refresh_date
    )
    select
        date_key,	
        utid,
        category_name,
        brand,
        model,
        issuer_bank,
        tenure_type,
        case when service_type is null then 'OTHERS' else service_type end as service_type, 
        case when credit_debit like '%CREDIT%' then 'CREDIT' when credit_debit is null then 'OTHERS' else credit_debit end as credit_debit, 
        product_type,
        -- count 
        count(distinct case when SALE_PRODUCT_VAL <> 0 then prim_id END) as SALE_PRODUCT_INVC_COUNT, 
        count(distinct case when SALE_TRX_VAL <> 0 then prim_id END) as SALE_TRX_INVC_COUNT, 
        count(distinct case when sale_trx_val_excluding_test_transactions <> 0 then prim_id END) as sale_trx_val_excluding_test_transactions_invc_count, 
        count(distinct case when SALE_NET_VAL <> 0 then prim_id END) as SALE_NET_INVC_COUNT, 
        count(distinct case when SALE_LOAN_VAL <> 0 then prim_id END) as SALE_LOAN_INVC_COUNT, 
        count(distinct case when SALE_EMI_VAL <> 0 then prim_id END) as SALE_EMI_INVC_COUNT, 
        count(distinct case when SALE_NOCOSTEMI_VAL <> 0 then prim_id END) as SALE_NOCOSTEMI_INVC_COUNT, 
        count( distinct case when SALE_GENIE_DISC_VAL <> 0 then prim_id END) as SALE_GENIE_DISC_INVC_COUNT, 
        count(distinct case when SALE_CASHBACK_DISC_VAL <> 0 then prim_id END) as SALE_CASHBACK_DISC_INVC_COUNT, 
        count(distinct case when SALE_EFT_VAL <> 0 then prim_id END) as SALE_EFT_INVC_COUNT, 
        count(distinct case when BANK_EMI_VAL <> 0 then prim_id END) as BANK_EMI_INVC_COUNT, 
        count(distinct case when BRAND_EMI_VAL <> 0 then prim_id END) as BRAND_EMI_INVC_COUNT, 
        count(distinct case when EXCLUSIVE_EMI_VAL <> 0 then prim_id END) as EXCLUSIVE_EMI_INVC_COUNT, 
        count(distinct case when WALLET_EMI_VAL <> 0 then prim_id END) as WALLET_EMI_INVC_COUNT, 
        count(distinct case when DC_EMI_VAL <> 0 then prim_id END) as DC_EMI_INVC_COUNT, 
        count(distinct case when INSTANT_DISCOUNT <> 0 then prim_id END) as INSTANT_DISCOUNT_INVC_COUNT, 
        count(distinct case when ADDITIONAL_CASHBACK <> 0 then prim_id END) as ADDITIONAL_CASHBACK_INVC_COUNT, 
        count(distinct case when upper(is_dcc_transaction)='YES' and transaction_type ='EFT DCC_SALE_LEG2'then prim_id end) as dcc_trx_count,
        sum(case when otp = 'NA' or otp is null then 0 else 1 end) as genie_coupon_count, 
        -- values 
        SUM(SALE_PRODUCT_VAL) as SALE_PRODUCT_VAL, 
        SUM(SALE_TRX_VAL) as SALE_TRX_VAL, 
        sum(sale_trx_val_excluding_test_transactions) as sale_trx_val_excluding_test_transactions,
        SUM(SALE_NET_VAL) as SALE_NET_VAL, 
        SUM(SALE_LOAN_VAL) as SALE_LOAN_VAL, 
        SUM(SALE_EMI_VAL) as SALE_EMI_VAL, 
        sum(SALE_NOCOSTEMI_VAL) as SALE_NOCOSTEMI_VAL, 
        SUM(SALE_GENIE_DISC_VAL) as SALE_GENIE_DISC_VAL, 
        SUM(SALE_CASHBACK_DISC_VAL) as SALE_CASHBACK_DISC_VAL, 
        SUM(emi_amount) as EMI_AMOUNT, 
        SUM (sale_eft_val) as sale_eft_val, 
        SUM (bank_emi_val) as bank_emi_val, 
        SUM (brand_emi_val) as brand_emi_val, 
        SUM (exclusive_emi_val) as exclusive_emi_val, 
        SUM (wallet_emi_val) as wallet_emi_val, 
        SUM (dc_emi_val) as dc_emi_val, 
        SUM (INSTANT_DISCOUNT) as INSTANT_DISCOUNT, 
        SUM (ADDITIONAL_CASHBACK) as ADDITIONAL_CASHBACK, 
        sum(case when upper(is_dcc_transaction)='YES' and transaction_type ='EFT DCC_SALE_LEG2'then sale_trx_val end) as dcc_trx_val,
        cast(current_date as date) as refresh_date 
    from (
        SELECT 
            prim_id, 
            UPPER(TRIM(
                case 
                    when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then 
                        coalesce (
                            cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiManufacturerName', 
                            cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiManufacturerName', 
                            cast(txn.addtnlinfo1 as JSON)-> 2 -> 'emiChargeSlipModel' ->> 'emiManufacturerName'
                        ) 
                    else 'Others' 
                end
            )) as brand, 
            UPPER(TRIM(
                case 
                    when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null  then 
                        coalesce (
                            cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiModelName', 
                            cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiModelName', 
                            cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiModelName'
                        ) 
                    else 'Others' 
                end
            )) as model,
            store_code,
            UPPER(TRIM(
                case 
                    when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then coalesce (
                        cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiCategoryName', 
                        cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiCategoryName', 
                        cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiCategoryName'
                        ) 
                    else 'Others' end
            )) as category_name,
            issuing_bank_name as issuer_bank,
            case 
                when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then
                    upper(coalesce(
                        cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiTenure',
                        cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiTenure',
                        cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiTenure',
                        '0') 
                    )
            end as tenure_type,
            to_char(transaction_date, 'YYYYMMDD')::int as date_key,
            upper(co_btid) as btid, 
            upper(utid) as utid, 
            txn.acq_bank_code, 
            date(transaction_date) AS sale_trans_date, 
            ci_tender_mode AS tender_mode, 
            UPPER(TRIM(
                case 
                    when concat(txn.ci_tender_mode, ' ', txn.transaction_type) = null then 'others' 
                    else concat(txn.ci_tender_mode, ' ', txn.transaction_type) 
                end
            )) as transaction_type, 
            (case when txn.transaction_type in ('DCC_SALE_LEG1', 'DCC_SALE_LEG2') then 'yes' else 'no' end) as is_dcc_transaction,
            UPPER(
            TRIM(
              cast(
                service_type as varchar(100)
              )
            )
            ) as service_type, 
            credit_debit, 
            txn.product_type, 
            txn.communication_id, 
            case 
                when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then (
                    coalesce(
                        case 
                            when txn.ci_inno_processingcode in ('510000', '500000') 
                            then coalesce(
                                (cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiEftTxnAmt')::decimal,
                                (cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiEftTxnAmt')::decimal,
                                (cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiEftTxnAmt')::decimal,
                                0
                            )
                            else coalesce((case when txn.ci_amount ~ '^[0-9\.]+$' then cast(txn.ci_amount as decimal) else 0 end) ::decimal/100, 0) 
                        end,
                      0
                    )
                ) else coalesce((case when txn.bi_amount ~ '^[0-9\.]+$' then cast(txn.bi_amount as decimal) else 0 end) ::decimal/100, 0) 
            end as sale_product_val,-- "Product Amount",
            case 
                when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then (
                coalesce(
                    case when txn.ci_inno_processingcode in ('510000', '500000') 
                        then coalesce(
                            (cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                            (cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                            (cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                            0
                        )
                        else coalesce(
                             (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 0 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                             (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 1 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                             (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 2 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                             (case when txn.bi_amount ~ '^[0-9\.]+$' then cast(txn.bi_amount as decimal) else 0 end)/100,
                             0
                             )
                        end,0
                    )
                ) else coalesce((case when txn.bi_amount ~ '^[0-9\.]+$' then cast(txn.bi_amount as decimal) else 0 end)/100, 0) end as sale_trx_val,-- "Transaction Amount"  
            case 
                when 
                    case 
                        when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then (
                        coalesce(
                            case when txn.ci_inno_processingcode in ('510000', '500000') 
                                then coalesce(
                                    (cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                                    (cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                                    (cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                                    0
                                )
                                else coalesce(
                                     (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 0 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                                     (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 1 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                                     (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 2 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                                     (case when txn.bi_amount ~ '^[0-9\.]+$' then cast(txn.bi_amount as decimal) else 0 end)/100,
                                     0
                                     )
                                end,0
                            )
                        ) else coalesce((case when txn.bi_amount ~ '^[0-9\.]+$' then cast(txn.bi_amount as decimal) else 0 end)/100, 0) end > 11 
                then 
                    case 
                        when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then (
                        coalesce(
                            case when txn.ci_inno_processingcode in ('510000', '500000') 
                                then coalesce(
                                    (cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                                    (cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                                    (cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                                    0
                                )
                                else coalesce(
                                     (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 0 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                                     (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 1 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                                     (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 2 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                                     (case when txn.bi_amount ~ '^[0-9\.]+$' then cast(txn.bi_amount as decimal) else 0 end)/100,
                                     0
                                     )
                                end,0
                            )
                        ) else coalesce((case when txn.bi_amount ~ '^[0-9\.]+$' then cast(txn.bi_amount as decimal) else 0 end)/100, 0) end
                else 0
            end as sale_trx_val_excluding_test_transactions,
            (case when ci_amount ~ '^[0-9\.]+$' then cast(ci_amount as decimal) else 0 end)/100 as sale_net_val, 
            case 
                when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then (
                case when txn.ci_inno_processingcode in ('510000', '500000') then 
                 coalesce(
                  cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiLoanAmt', 
                  cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiLoanAmt', 
                  cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiLoanAmt', 
                  '0'
                ):: decimal else 0 end
                ) else 0  
            end as SALE_LOAN_VAL, 
            coalesce(
                (
                    case when upper(ci_tender_mode) like 'EMI%%' 
                    then 
                        case 
                        when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then (
                        coalesce(
                            case when txn.ci_inno_processingcode in ('510000', '500000') 
                                then coalesce(
                                    (cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                                    (cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                                    (cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiTxnAmt')::decimal,
                                    0
                                )
                                else coalesce(
                                     (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 0 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                                     (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 1 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                                     (regexp_replace(txn.addtnlinfo1::text, E'[\\n\\r]+', ' ', 'g' )::json -> 2 -> 'magicOTPRewards' ->> 'saleAmt')::decimal,
                                     (case when txn.bi_amount ~ '^[0-9\.]+$' then cast(txn.bi_amount as decimal) else 0 end)/100,
                                     0
                                     )
                                end,0
                            )
                        ) else coalesce((case when txn.bi_amount ~ '^[0-9\.]+$' then cast(txn.bi_amount as decimal) else 0 end)/100, 0) end
                    end
                ), 
                0
            ) as SALE_EMI_VAL, 
            case when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then (
                case when txn.ci_inno_processingcode in ('510000', '500000') then 
                coalesce (
                  cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiTxnEmiAmt', 
                  cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiTxnEmiAmt', 
                  cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiTxnEmiAmt', 
                  '0'
                ):: decimal else 0 end
            )  else 0 end as emi_amount, 
            case when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then (
                case when txn.ci_inno_processingcode in ('510000', '500000') then 
                coalesce(
                  (cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiCashbackAmt'), 
                  (cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiCashbackAmt'), 
                  (cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiCashbackAmt'), 
                  '0'
                ):: decimal else 0 end
            )  else 0 end as SALE_NOCOSTEMI_VAL, 
            case when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then (
                case when txn.ci_inno_processingcode in ('510000', '500000') then coalesce (
                  (
                    regexp_replace(
                      txn.addtnlinfo1 :: text, E'[\\n\\r]+', 
                      ' ', 'g'
                    ):: json -> 0 -> 'magicOTPRewards' ->> 'rwdAmt'
                  ):: decimal, 
                  (
                    regexp_replace(
                      txn.addtnlinfo1 :: text, E'[\\n\\r]+', 
                      ' ', 'g'
                    ):: json -> 1 -> 'magicOTPRewards' ->> 'rwdAmt'
                  ):: decimal, 
                  (
                    regexp_replace(
                      txn.addtnlinfo1 :: text, E'[\\n\\r]+', 
                      ' ', 'g'
                    ):: json -> 2 -> 'magicOTPRewards' ->> 'rwdAmt'
                  ):: decimal, 
                  0
                ) else coalesce (
                  (
                    regexp_replace(txn.addtnlinfo1 :: text, E'[\\n\\r]+',' ', 'g'):: json -> 0 -> 'magicOTPRewards' ->> 'rwdAmt'):: decimal, 
                  (
                    regexp_replace(txn.addtnlinfo1 :: text, E'[\\n\\r]+',' ', 'g'):: json -> 1 -> 'magicOTPRewards' ->> 'rwdAmt'):: decimal, 
                  (
                    regexp_replace(
                      txn.addtnlinfo1 :: text, E'[\\n\\r]+', 
                      ' ', 'g'
                    ):: json -> 2 -> 'magicOTPRewards' ->> 'rwdAmt'
                  ):: decimal, 
                  0
                ) end
            ) else 0  end as SALE_GENIE_DISC_VAL, 
            case when is_valid_json(txn.addtnlinfo1) or txn.addtnlinfo1 is null then (
                case WHEN coalesce(
                  cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiUpfrontAmt', 
                  cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiUpfrontAmt', 
                  cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiUpfrontAmt', 
                  txn.addtnlinfo1 :: json -> 0 ->> 'cashBackAmount', 
                  txn.addtnlinfo1 :: json -> 1 ->> 'cashBackAmount', 
                  txn.addtnlinfo1 :: json -> 2 ->> 'cashBackAmount', 
                  '0'
                )= 'NA' then 0 else cast(
                  coalesce(
                    cast(txn.addtnlinfo1 as JSON) -> 0 -> 'emiChargeSlipModel' ->> 'emiUpfrontAmt', 
                    cast(txn.addtnlinfo1 as JSON) -> 1 -> 'emiChargeSlipModel' ->> 'emiUpfrontAmt', 
                    cast(txn.addtnlinfo1 as JSON) -> 2 -> 'emiChargeSlipModel' ->> 'emiUpfrontAmt', 
                    txn.addtnlinfo1 :: json -> 0 ->> 'cashBackAmount', 
                    txn.addtnlinfo1 :: json -> 1 ->> 'cashBackAmount', 
                    txn.addtnlinfo1 :: json -> 2 ->> 'cashBackAmount', 
                    '0'
                  ) as decimal
                ) end
            ) else 0  end as SALE_CASHBACK_DISC_VAL, 
            ----how do diff between cashback and instat discount
            amount, 
            Case when "transaction_result" = 'SALE' then
                case when is_valid_json(addtnlinfo1) is true or is_valid_json(addtnlinfo1) is null  
                    then coalesce(
                            addtnlinfo1::json->0 -> 'magicOTPRewards' ->> 'gntdOtp',
                            addtnlinfo1::json->1 -> 'magicOTPRewards' ->> 'gntdOtp',
                            addtnlinfo1::json->2 -> 'magicOTPRewards' ->> 'gntdOtp'
                        )
                    else 
                        null
                end
            end	otp, 
            case when is_valid_json(txn.addtnlinfo1) then txn.addtnlinfo1 end as addtnlinfo1, 
            ci_inno_processingcode, 
            case
                when ci_tender_mode = 'EFT'
                then amount::decimal
                else 0
            end SALE_EFT_VAL, 
            (
            case when is_valid_json(addtnlinfo1) then
                    case 
                    when (
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                    ) like ('BRA%')
                    or	(
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                    ) not like ('BRA%')
                    and
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                    ) not like ('TOT%')
                    and
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                    ) not like ('BAN%')
                    and
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                    ) not like ('EXC%')
                    and 
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiTxnType'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiTxnType'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiTxnType')
                     )  like ('%BRAND%')
                    )
                    )
                    then amount::decimal
                    else 0
                    end
                end
            ) brand_emi_val, 
            (
                case when is_valid_json(addtnlinfo1) then
                       case	when (
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) like ('BAN%')
                or	(
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                    ) not like ('BRA%')
                    and
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                    ) not like ('TOT%')
                    and
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                    ) not like ('BAN%')
                    and
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                    ) not like ('EXC%')
                    and 
                    coalesce (
                        (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiTxnType'),
                        (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiTxnType'),
                        (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiTxnType')
                     )  like ('%BANK%')
                )
                )
                then amount::decimal
                else 0
                end
            end) BANK_EMI_VAL, 
            (
            case
                when is_valid_json(addtnlinfo1) and (
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) like ('EXC%')
                or	(
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) not like ('BRA%')
                and
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) not like ('TOT%')
                and
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) not like ('BAN%')
                and
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) not like ('EXC%')
                and 
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiTxnType'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiTxnType'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiTxnType')
                 )  like ('%EXCLUSIVE%')
                )
                ) 
                then amount::decimal
                else 0
            end) EXCLUSIVE_EMI_VAL, 
            (
                case
                    when is_valid_json(addtnlinfo1) and (
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) like ('TOT%')
                or	(
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) not like ('BRA%')
                and
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) not like ('TOT%')
                and
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) not like ('BAN%')
                and
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiSchemeCode'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiSchemeCode')
                ) not like ('EXC%')
                and 
                coalesce (
                    (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiTxnType'),
                    (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiTxnType'),
                    (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiTxnType')
                 )  like ('%FREE%')
                )
                )
                then amount::decimal
                else 0
            end) WALLET_EMI_VAL, 
            (
                case when ci_inno_processingcode = '510000'
                    then amount::decimal
                    else 0
                end
            ) DC_EMI_VAL, 
            case when is_valid_json(addtnlinfo1) then
            coalesce (
                (addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiInstantDiscAmnt'),
                (addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiInstantDiscAmnt'),
                (addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiInstantDiscAmnt'),
                '0'
            )::numeric
            end INSTANT_DISCOUNT, 
            case 
                when is_valid_json(addtnlinfo1) then 
                    case
                    -- condition 1 % upto
                    when split_part(coalesce (
                            addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                            addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                            addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention'
                            ), '#', 2
                        ) like '%\%%'
                        and split_part(coalesce (
                            addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                            addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                            addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention'
                            ), '#', 2
                        ) like '%upto%'
                    then
                        least(
                            (
                                amount * (
                                    split_part(split_part(coalesce (
                                        addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                                        addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                                        addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention'
                                    ), '#', 2), '%', 1)::numeric / 100
                                )::numeric
                            )
                            ,
                            (   split_part(split_part(coalesce (
                                    addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                                    addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                                    addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention'
                                    ), '#', 2), 'Rs', 2
                                )::numeric
                            )
                        )
                    -- condition 2 % flat
                    when split_part(coalesce (
                            addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                            addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                            addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention'
                            ), '#', 2
                        ) like '%\%%'
                    then
                        amount * (
                            split_part(split_part(coalesce (
                                addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                                addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                                addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention'
                            ), '#', 2), '%', 1)::numeric / 100
                        )::numeric
                    -- condition 3 flat
                    else
                        coalesce(
                            split_part(split_part(coalesce (
                                addtnlinfo1::json -> 0 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                                addtnlinfo1::json -> 1 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention',
                                addtnlinfo1::json -> 2 -> 'emiChargeSlipModel' ->> 'emiAddtnlSubvention'
                                ), '#', 2), 'Rs', 2
                            )::numeric,
                            case 
                            when 
                                coalesce (
                                    addtnlinfo1::json -> 0 ->> 'cashBackAmount',
                                    addtnlinfo1::json -> 1 ->> 'cashBackAmount',
                                    addtnlinfo1::json -> 2 ->> 'cashBackAmount'
                                ) = 'NA' then '0.00'::numeric
                                else
                                coalesce (
                                    addtnlinfo1::json -> 0 ->> 'cashBackAmount',
                                    addtnlinfo1::json -> 1 ->> 'cashBackAmount',
                                    addtnlinfo1::json -> 2 ->> 'cashBackAmount'
                                )::numeric
                                end, 
                            '0.00'::numeric
                        )
                end::numeric
            end ADDITIONAL_CASHBACK 
        from edw_sparcs.report_daily_transaction_{transaction_date} txn 
        where transaction_result = 'SALE'
    ) foo
    group by 
    date_key,	
        utid,
        category_name,
        brand,
        model,
        issuer_bank,
        credit_debit,
        tenure_type,
        service_type,
        product_type
    ;
    """.format(transaction_date=''.join(str(for_date).split('-')))
    cur.execute(query)
    cur.close()
    print("Data Added for {}".format(for_date))

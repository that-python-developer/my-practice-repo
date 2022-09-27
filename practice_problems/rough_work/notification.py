import json
import requests
import datetime #for current timestamps

python_process_name = 'load_data_google_sheet_genie_lead_details'
start_time = datetime.datetime.now() # start process logs

notification_url = 'http://172.25.148.131:12345/notification/sendSmsToContacts'

mobile_numbers = ['918766523312']
content = ''

input_json = {
    'mobileNumber': mobile_numbers,
    'smsContent': content
}

res = requests.post(
    notification_url,
    data=json.dumps(input_json)
)

response = json.loads(res.text)


end_time = datetime.datetime.now()
delta = end_time - start_time

print('success!')

import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel, InputPeerChat
from telethon import TelegramClient, sync, events

# get your api_id, api_hash, token from telegram as described above
api_id = 16436656
api_hash = 'a7aa126fe29e5c716332064cb6880973'
token = '5324128381:AAH-KTHnk1nMPFKPwVqhBPn_ipd8_9RQP38'
message = "Worked Successful!!"

# your phone number
phone = '+918766523319'

# creating a telegram session and assigning it to a variable client
client = TelegramClient('session', api_id, api_hash)

# connecting and building the session
client.connect()

# in case of script ran first time it will ask either to input token or otp sent to number or sent or your telegram id
if not client.is_user_authorized():
    client.send_code_request(phone)

    # signing in the client
    client.sign_in(phone, input('Enter the code: '))

try:
    # receiver user_id and access_hash, use
    # my user_id and access_hash for reference

    receiver = InputPeerUser(1718547619, 0) # Advait
    # receiver = InputPeerUser(1524042333, 0) # Rohit

    # sending message using telegram client
    client.send_message(receiver, message, parse_mode='html')

except Exception as e:
    # there may be many error coming in while like peer error, wrong access_hash, flood_error, etc
    print(e)

# disconnecting the telegram session
client.disconnect()

import os
import requests
import json
import math
from urllib.parse import urlencode


from twilio.rest import Client


url = "https://api.nomics.com/v1/"
nomics_api_key = os.environ['NOMICS_API_KEY']
query_object = {
    "key": nomics_api_key,
    "ids": "BTC",
    "convert": "USD"
}

qs = urlencode(query_object)
print(qs)

r = requests.get(url+"currencies/ticker?"+qs)
# json_object = r.json()[0]
data = r.json()
string = json.dumps(data)
decoded = json.loads(string)
price = math.trunc(float(decoded[0]["price"]))
one_day = math.trunc(float(decoded[0]["1d"]["price_change"]))
one_day_percent = int(float(decoded[0]["1d"]["price_change_pct"]))

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
print(account_sid)
client = Client(account_sid, auth_token)

to_send = None

if one_day_percent > 0:
    to_send = f'Bitcoin is up {one_day_percent}% (${one_day}) since yesterday. The current price is ${price}.'
elif one_day_percent < 0:
    to_send = f'Bitcoin is down {one_day_percent}% (${one_day}) since yesterday. The current price is ${price}.'
else:
    to_send = f'Bitcoin is basically unch. The current price is ${price}.'


print(to_send)

message = client.messages \
                .create(
                    body=to_send,
                    from_='+13158645501',
                    to='+13157967653'
                )

import os
import requests
import json
import math
from urllib.parse import urlencode

from twilio.rest import Client


def get_prices_generate_messages(quote, convert):

    # nomics endpoint
    url = "https://api.nomics.com/v1/"

    # nomics_api_key = os.environ['NOMICS_API_KEY']
    nomics_api_key = 'f348b9100f67d8eb4c5cfd89cd16d999'

    query_object = {
        "key": nomics_api_key,
        "ids": quote,
        "convert": convert
    }

    qs = urlencode(query_object)

    r = requests.get(url+"currencies/ticker?"+qs)

    data = r.json()
    string = json.dumps(data)
    decoded = json.loads(string)
    price = math.trunc(float(decoded[0]["price"]))
    one_day = math.trunc(float(decoded[0]["1d"]["price_change"]))
    one_day_percent = int(float(decoded[0]["1d"]["price_change_pct"]))

    to_send = None

    if one_day_percent > 0:
        to_send = f'Bitcoin is up {one_day_percent}% (${one_day}) since yesterday. The current price is ${price}.'
    elif one_day_percent < 0:
        to_send = f'Bitcoin is down {one_day_percent}% (${one_day}) since yesterday. The current price is ${price}.'
    else:
        to_send = f'Bitcoin is basically unch. The current price is ${price}.'

    return to_send


# twilio account config
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)


def send_message(message, number):
    message = client.messages \
                    .create(
                        body=to_send,
                        from_='+13158645501',
                        to=number
                    )

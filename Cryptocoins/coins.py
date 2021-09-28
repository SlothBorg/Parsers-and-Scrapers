import urllib.request
import json
from datetime import datetime

baseURL = 'https://api.cryptonator.com/api/ticker/'
coins = ['btc', 'eth', 'ltc', 'mco', 'neo']
# Example API return
# {
#     'ticker':
#         {
#             'base': 'LTC',
#             'target': 'USD',
#             'price': '66.34627682',
#             'change': '0.26714253'
#         },
#     'timestamp': 1504182602,
#     'success': True,
#     'error': ''
# }

for coin in coins:
    URL = baseURL + coin + '-usd'
    response = urllib.request.urlopen(URL).read()
    jsonResponse = json.loads(response.decode('utf-8'))
    if (jsonResponse['success']):
        # Print the time that the data is from
        time = datetime.fromtimestamp(jsonResponse['timestamp'])
        print("As of %s:%s %02d:" % (time.hour, time.minute, time.second), end='')
        print("\t" + coin.upper() + "\t$" + jsonResponse['ticker']['price'] + "\t$" + jsonResponse['ticker']['change'])
    else:
        print('success: ' + jsonResponse['success'])
        print('ERROR: ' + jsonResponse['error'])

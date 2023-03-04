import requests
import json

url = 'https://min-api.cryptocompare.com/data/v2/histohour'
params = {'fsym': 'BTC', 'tsym': 'USD', 'limit': '10', 'aggregate': '1'}

headers = {'authorization': 'Your-API-Key'}

response = requests.post(url, params=params, headers=headers)

if response.status_code == 200:
    data = json.loads(response.content)
    print(data)
else:
    print("Error: could not retrieve data.")

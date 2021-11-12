#Retrieve data from the coinbase websocekt API
import requests
import json
import csv
from websocket import create_connection
import time
import pandas as pd


BTC_price = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
ETH_price = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'

#pull data from coinbase API
def get_data(url):
    response = requests.get(url)
    data = response.json()
    print(data)

get_data('https://api.coinbase.com/v2/prices/BTC-USD/spot')
get_data('https://api.coinbase.com/v2/prices/ETH-USD/spot')

#Calculate ETH-BTC price
def get_difference(url1, url2):
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    data1 = response1.json()
    data2 = response2.json()
    price1 = float(data1['data']['amount'])
    price2 = float(data2['data']['amount'])
    difference = price2 / price1
    print(f'1 ETH Price is equal to {difference} BTC')

get_difference(BTC_price, ETH_price)
'''Calculate the VWAP per trading pair using a sliding window of 200 data points. Meaning, when a new
data point arrives through the websocket feed the oldest data point will fall off and the new one will be
added such that no more than 200 data points are included in the calculation.'''


#Websocket feed coinbase API

URL = "wss://ws-feed.pro.coinbase.com"

ws = create_connection(URL)


params = {"type": "subscribe", "product_ids": ["BTC-USD"],
"channels": ["heartbeat", {"name": "ticker", "product_ids": ["BTC-USD"]}]}

counter = 0
f = open('VMAP_Data.json', 'a')
while True:
    ws.send(json.dumps(params))
    result = ws.recv()
    print(result)

    time.sleep(1)

    csv_file = csv.writer(f)
    csv_file.writerow([result])
    # for item in converted['price']:
    #     price = csv_file.writerow([item['price']])
    #     csv_file.writerow(price)
    counter += 1
    if counter == 5:
        f.close()
        break


ws.close()


# Read the csv file
data = pd.read_csv('VMAP_Data.csv')

# Print it out if you want
print(data)


df = pd.read_json('VMAP_Data.json')

# data = df.to_json()
print(df)

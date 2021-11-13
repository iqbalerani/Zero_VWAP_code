#Retrieve data from the coinbase websocekt API
import requests
import json
import csv
from websocket import create_connection
import time
import pandas as pd


BTC_price = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
ETH_price = 'https://api.coinbase.com/v2/prices/ETH-USD/spot'

'''pull data from coinbase API'''

def get_data(url):
    response = requests.get(url)
    data = response.json()
    print(data)

get_data('https://api.coinbase.com/v2/prices/BTC-USD/spot')
get_data('https://api.coinbase.com/v2/prices/ETH-USD/spot')

'''Calculate ETH-BTC price'''

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

# Websocket feed coinbase API

URL = "wss://ws-feed.pro.coinbase.com"

ws = create_connection(URL)


params = {"type": "subscribe", "product_ids": ["BTC-USD"],
"channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}]}

counter = 0

while True:
    ws.send(json.dumps(params))
    result = ws.recv()

    time.sleep(1)

    with open('Data_Points.json', 'a') as jf:
        json.loads(result)
        jf.write(result)

        jf.write('\n')

    # 200 Data Points fetched from API
    counter += 1
    if counter == 200:
        break


ws.close()


''' Read the line and then convert each line values into one excel spreadsheet format '''

with open('Data_Points.json', 'r') as f:
    j = 0
    for line in f:

        a = json.loads(line)

        #create each row in the csv file
        with open('Data_Points.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            if j <= 1:
                writer.writerow(a)
                j += 1
            writer.writerow(a.values())


'''   Clean the data before running the VWAP calculation - Delete empty rows and bring the header at the top        '''
'''Using pandas to read the csv file and calculate the VWAP by first calculating the sum of the price and volume
# and then dividing the sum by the volume.'''


# def VWAP():
#     data = pd.read_csv('Data_Points.csv')
#     VWAP = data['price'].sum() * data['volume_30d'] / data['volume_30d'].sum()
#     print(f'Volume Weighted Average Price')
#     print(VWAP)
#
# VWAP()

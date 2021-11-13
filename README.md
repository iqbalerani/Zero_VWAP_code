# Zero_VWAP_code

Problem Specification:
● Retrieve a data feed from the coinbase websocket and subscribe to the matches channel. Pull data for
the following three trading pairs:
○ BTC-USD
○ ETH-USD
○ ETH-BTC
● Calculate the VWAP per trading pair using a sliding window of 200 data points. Meaning, when a new
data point arrives through the websocket feed the oldest data point will fall off and the new one will be
added such that no more than 200 data points are included in the calculation.
○ The first 200 updates will have less than 200 data points included. That’s fine for this project.
● Stream the resulting VWAP values on each websocket update.
○ Print to stdout or file is ok. Usually you would send them off through a message broker but a
simple print is perfect for this project.

Solution:

1- '''pull data from coinbase API'''
2- '''Calculate ETH-BTC price'''
3- '''Calculate the VWAP per trading pair using a sliding window of 200 data points. Meaning, when a new
data point arrives through the websocket feed the oldest data point will fall off and the new one will be
added such that no more than 200 data points are included in the calculation.'''
4- ''' Read the line and then convert each line values into one excel spreadsheet format '''
5- '''   Clean the data before running the VWAP calculation - Delete empty rows and bring the header at the top        '''
'''Using pandas to read the csv file and calculate the VWAP by first calculating the sum of the price and volume
and then dividing the sum by the volume.'''

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

1- With API of coinbase is calculated first the BTC-USD, ETH-USD, and finally ETH-BTC. On Second and Third by subscribing the API Coinbase we have fetched the sliding window 200 data points.
2- 

"""
This file houses the backend for the financial dashboard project.
It takes in search queries from the frontend as an input and outputs
a JSON file with formatted stock Ticker data.
"""

## Libraries ##
import yfinance as yf       # fetching stock data
import pandas as pd         # calculating daily mean return
import json                 # turn raw data into formatted data for frontend

## 1. Get search query ##

def getSearchQuery():
    pass # not to be implemented yet due to frontend not being made

query = "TSLA"

## 2. Create yfinance ticker ##

stockTicker = yf.Ticker(query)

## 3. Get price history ##

priceHistory = stockTicker.history(period="1m")         # get the history for 1 month
priceHistory = priceHistory.reset_index()               # reset the indexes to make it formattable

## 4. Extra information ##

extraInfoData = stockTicker.fast_info       # download database of all information today

# Assign each variable a unique datapoint
openingPrice = extraInfoData.get("open")
prevClosingPrice = extraInfoData.get("previousClose")
dailyHigh = extraInfoData.get("dayHigh")
dailyLow = extraInfoData.get("dayLow")
volume = extraInfoData.get("lastVolume")
marketCap = extraInfoData.get("marketCap")

## 5. Daily mean return using pandas ##

dailyReturns = priceHistory["close"].pct_change()
meanDailyReturn = dailyReturns.mean()




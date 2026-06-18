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

"""
This function fetches all of the stock data and puts it into the JSON file.
"""
def getStockData(stock: str, timePeriod: str):
    ## 2. Create yfinance ticker ##
    stockTicker = yf.Ticker(stock)

    ## 3. Get price history ##
    priceHistory = stockTicker.history(period=timePeriod)   # get the history for 1 month
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
    dailyReturns = priceHistory["Close"].pct_change()
    meanDailyReturn = dailyReturns.mean()

    ## 6. Pack data into JSON ##
    historyJSON = priceHistory.to_json(orient="records", date_format="iso") # Raw data -> JSON string
    historyData = json.loads(historyJSON) # JSON string -> list

    JSONPackage = {
        "metadata": {
            "ticker": stock,
            "open": openingPrice,
            "previousClose": prevClosingPrice,
            "high": dailyHigh,
            "low": dailyLow,
            "volume": volume,
            "marketCap": marketCap,
            "meanDailyReturn": meanDailyReturn
        },
        "history": historyData
    }

    # Write to JSON
    with open("data.json", "w") as file:
        json.dump(JSONPackage, file, indent=4)


getStockData(query, "1mo")


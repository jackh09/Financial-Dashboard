# Design
## Introduction
This document will be the planning phase of this project, allowing me to sketch out some of the algorithms and elements of the project.

## Backend
### Designing the backend first
I will design the backend of this project first. I have multiple reasons for doing this is, they are:
1. I am a lot more comfortable in coding backend algorithms
2. I have a lot more experience in Python than HTML, CSS and Javascript
3. It will help me build my frontend around the json file that this program will create

### General Backend Flow
The whole point of this backend design is to turn a search query into useable data for the frontend. Hence program flow will be as follows:
1. Search query recieved from the frontend
2. yfinance ticker for that stock will be initialised (an error will be returned if it is an invalid stock name)
3. Price history for the specific time range will be fetched
4. Extra information will be fetched
5. Pandas used to calculate daily mean return
6. Data packed into a json
7. Updated every minute
I now have 7 unique, abstracted steps that I can use to develop my backend.

### 1. Search Query
* Frontend will paste the search command into a "searchquery.json" file
* Simultaneously, the search bar will run the Python script
* The first thing that the Python file will do is access the JSON file and get the query.

### 2. yfinance Ticker
* yfinance ticker will be initialised
```python
import yfinance as yf
## Get search query
stockTicker = yf.Ticker(query)
## Data queries can now be made on this yf.Ticker object
```

### 3. Price History
* yfinance will fetch the history of the stock at a pre-set range of 1 month.
* This can be changed by the user but for simplicity, it will use this interval first.
* The index will be reset on this data so that pandas can analyse it and it can be put into JSON format
```python
priceHistory = stockTicker.history(period="1m") # Fetch stock history in past month
priceHistory = priceHistory.reset_index() # Reset index for pandas + JSON
```

### 4. Extra information
* From the analysis stage, one of my success criteria was to fetch the following:
* Opening price, previous closing price, daily high/low, volume, market cap
* These can be fetched very easily using yfinance
```python
extraInfoData = stockTicker.fast_info # Download the dataframe of all the data within a day
# Assign each variable a singular datapoint
openingPrice = extraInfoData.get("open")
prevClosingPrice = extraInfoData.get("previousClose")
dailyHigh = extraInfoData.get("dayHigh")
dailyLow = extraInfoData.get("dayLow")
volume = extraInfoData.get("lastVolume")
marketCap = extraInfoData.get("marketCap")
```

### 5. Daily mean return using pandas
* Self-explanatory
```python
# pandas already imported as pd
dailyReturns = priceHistory["Close"].pct_change()
meanDailyReturn = dailyReturns.mean()
```

### 6. Data packed into JSON file
* All of this data now needs to be packed into a JSON file to send off to the frontend

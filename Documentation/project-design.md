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
I now have 7 unique, abstracted steps that I can use to develop my backend. Furthermore, this can all be placed in a function to run multiple times.

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
```python
import json

history_json = priceHistory.to_json(orient="records", date_format="iso") # Raw data to JSON string
history_data = json.loads(history_json) # Turn string into a list

JSONPackage = {
    "metadata": {
        "ticker": query,
        "open": openingPrice,
        "previousClose": prevClosingPrice,
        "high": dailyHigh,
        "low": dailyLow,
        "volume": volume,
        "marketCap": marketCap,
        "meanDailyReturn": meanDailyReturn
    },
    "history": history_data
}

# Write to the JSON file
with open("data.json", "w") as file:
    json.dump(JSONPackage, file, indent=4)
```

### 7. Update every minute
* Wait for one minute
* Get new period
* Refresh using a function
```python
import time
time.sleep(60.5) # Give a bit of leeway so that it actually updates
getStockData(query, newperiod)
```

## Frontend
I will now design the frontend. This will consist of 2 separate pages:
1. A landing page/search page
2. A stock viewer page

### Landing page
I will develop the landing page first as it is static and shouldn't be too difficult as my first HTML product.
By recalling the success criteria:
1. Website title at top
2. Short description explaining program and use cases
3. Search bar to find different stocks
4. Search bar input validation
I have 4 simple things that I need to develop.

#### 1. Website title
Firstly, I will make a website title. However, before doing so I will define some of the key parts of the HTML site:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Financial Dashboard</title>
</head>
</html> <!-- Remove this as it is only to make this section of code technically correct -->
```

Now to make the title; this can be easily done using headers:
```html
<body>
    <h1>Financial Dashboard / Stock Viewer</h1>
</body>
```

#### 2. Short description
Now to add a short description just below to introduce the project:
```html
<body>
    <p>
        This website hosts my financial dashboard/stock viewer project.<br>
        It is one project of a trilogy that I aim to accomplish before the start of the 2026/27 academic year.<br>
        The project itself is a full stack project that fetches financial data and displays data about it in a visual way.<br>
        It uses modules such as yfinance, json and charts.js and has a polyglot codebase (Python, HTML, CSS, Javascript).<br>
        A search bar is below this text: search up a stock name (e.g. AMZN, TSLA, AAPL) to bring up the stock viewer page for your chosen search.
    </p>
</body>
```

#### 3. Search bar
Now I will implement a simple search bar to allow the user to search for and look at financial data for their chosen stock:
```html
<body>
    <label for="Search">Search for a stock:</label><br>
    <input type="text" id="Search" name="Search" placeholder="TSLA">
    <input type="submit" value="Search">    
</body>
```

#### 4. Input validation
I can add input validation to my input to prevent erroneous data from being inputted. Furthermore, I have now
put each new attribute on a new line as this one line has quite a few:
```html
<body>
    <input
        type="text"
        id="Search"
        name="Search"
        placeholder="TSLA"
        required
        minlength="1"
        maxlength="10"
        pattern="[A-Za-z0-9\.\-=]+"
        title="Please enter a valid ticker symbol (e.g., TSLA, BTC-USD, VOD.L)"> <!-- Appears if user types an erroneous character -->
</body>
```

Now the main structure of the landing page is completete. Below is a screenshot of the final product (index.html):
![index.html screenshot](/Documentation/Assets/index-html-landing-page-screenshot-20-06-2026.png)

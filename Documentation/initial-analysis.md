# Initial analysis

## Project Introduction
This repository intends to document and present my financial dashboard project, coded using a mixture of different programming languages.
The project itself will be fairly basic: just allowing the user to check the financial history of different stocks, as well as providing some simple search features such as changing the time period, stock, data types, etc.
For this project, I will vaguely follow the OCR A-level project mark scheme and project guidance as the iterative approach is what I am used to using and works well for most projects.
I will use a very compressed approach though for my documentation, as I want to showcase my programming skills, not my essay-writing skills. To add to this, I will omit some sections that would have originally been compulsory in the project, for example an extensive breakdown of existing designs and stakeholder analysis, due to this project being unlikely to be used by consumers and also to get the project done in good time.
This project is one of 3 passion projects intended to develop my full stack skills via programming languages such as HTML, CSS, Javascript, Python and C++.

## Essential Ideas
As taught in my A-level Computer Science course, I will identify some essential ideas before doing anything else.
This will help me visualise the program as a whole in my head, and this clearer picture will aid in developing each module of the program as I will be able to consider preconditions, inputs and outputs beforehand.
This section will be split into 2 sections: one for the frontend and one for the backend.

### Frontend
* Landing page - tell the user about the project and how to use it
* Tool page - the webpage of which the financial dashboard will actually be hosted
* Various viewing methods - the ability to view the stock's histories in graphs or tables, as well as being able to see the stock's complicated data individually in a list
* Filtering by custom parameters - leading on from the previous point, the user should be able to filter by just one item, for example a stock's total loss/gain per day

### Backend
* Fetch live, accurate financial data
* Pack stock data into a json file for the website
* Efficient algorithms - attempt to reduce time and space complexity as much as possible
* Connect seamlessly with the website

## Limitations
I will now identify some limitations I may have/face. This is done in order to draw boundaries and prevent project-ending scope creep.
There aren't that many because I think this project is fairly simple and straightforward, however identifying them is good practice for projects in which I will face limitations.
* Expertise - although the project is very simple, the frontend may give me some problems as I have very limited experience in HTML/CSS/JS. However, the Python-based backend should be fine, as long as I read up on module documentation and take things slowly
  - Furthermore, I may run into some trouble trying to figure out how to make the front and backend link up as they use different programming languages.
* Time - my aim is to try and get all 3 of these projects done by the end of year 12 summer holidays, however this is just an arbitrary deadline and not set in stone

## Solution requirements
This program is, as stated a plethora of times before this point, fairly simple, so the program doesn't have many requirements. The user will need the following:
* Up-to-date web browser - to run the website frontend
* Stable internet connection - to enable the Python backend to retrieve market data without connection errors

## Preliminary research to inform success criteria
I will now look at some designs in brief to help plan out my success criteria. I will carry this out in the analysis stage as I don't want to walk into a project with my success criteria underdeveloped.

### Yahoo Finance
![Yahoo Finance Dashboard](/Assets/yahoo-finance-dashboard.png)
Yahoo Finance is an established platform for viewing tickers, and I will take some notes from their design, using reference from the image above.
* The page is dominated by the price graph, as it is the centerpiece for viewing a stock's history
* Attention to detail - the price scale on the graph is anchored to the right to make viewing the price of a stock easier without having to drag my eyes across the screen to read something on the left
* Also inside the graph section is a time selection menu: Yahoo Finance gives the user the option to choose 1D, 5D, 1M, 6M, YTD (year to date, start of fiscal year), 1Y, 5Y and all. I like this, it is simple and approachable but I think I will go for a more customisable option, giving users a number box to fill in
* The graph is also real time. I will definitely want this for my project which is why I defined a stable internet connection as one of my requirements
* Just underneath the graph, there is some additional information about the stock, including ranges, opening and closing prices and averages. This should be easy to implement using the yfinance module as it will just include setting some parameters
* Finally, there are some trending tickers. I think I will implement this by just selecting the stocks with the most volume that day

Overall, my design will be heavily based off Yahoo Finance as their UI is clean and easy to use. Some parts will obviously not be included for now, for example, news because I'm not a news outlet like Yahoo is.

### Financial Times
![Financial Times Indice Viewer](/Assets/financial-times-indice-viewer.png)
Next up I will look at the Financial Times. They have a more simplistic UI as compared to Yahoo Finance, which will suit my HTML/CSS skills better. It shares most of the same features as the Yahoo Finance Dashboard, however there are a couple of things that I would like to point out.
* Colour scheme - clear green/red for gain/loss
* Expanded data titles - no abbreviations, makes things easier to interpret

### yfinance
yfinance is a python module that I will use to build my backend: fetching market data and ticker requests, along with searches and streaming live market data.

I will leave research here, as I now have enough information to inform my success criteria.

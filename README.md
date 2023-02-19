# 

Welcome to the Cryptocurrency Price Prediction Tool! This tool uses machine learning to predict the price of a cryptocurrency over a selected time period. It retrieves historical price data from the CryptoCompare API, trains a linear regression model on that data, and generates price predictions for the selected time period.

## Technical Description

This tool is written in Python and uses the following libraries and APIs:

- Requests (to make HTTP requests to the CryptoCompare API)
- OpenPyXL (to create and modify Excel spreadsheets)
- Scikit-learn (to train and use the machine learning model)
- Colorama (to add color to the console output)

The tool prompts the user to select a cryptocurrency and time period to analyze, then retrieves historical price data from the CryptoCompare API. It uses Scikit-learn to train a linear regression model on the price data, then generates price predictions for the selected time period. The predictions are written to an Excel spreadsheet, which is saved in the "reports" folder.

## Architecture

High-level architecture diagram for the Cryptocurrency Price Prediction Tool:

        +-------------------+
        |                   |
        |  Cryptocurrency   |
        |     API Server    |
        |                   |
        +-------------------+
                 | HTTP Request
                 |
                 v
        +-------------------+
        |                   |
        |   Cryptocurrency  |
        |    Price Data     |
        |   Aggregation     |
        |                   |
        +-------------------+
                 |
                 | Historical Price Data
                 v
        +-------------------+
        |                   |
        |  Machine Learning |
        |   Price Predictor |
        |                   |
        +-------------------+
                 | Price Predictions
                 |
                 v
        +-------------------+
        |                   |
        |      Excel        |
        |  Price Predictions|
        |     Generator     |
        |                   |
        +-------------------+


## Installation

To install the Cryptocurrency Price Prediction Tool, follow these steps:

1. Clone the repository: git clone https://github.com/ovinokurov/PricePrediction.git
2. Install the required libraries: pip install requests openpyxl scikit-learn colorama
3. Run the tool: python main.py

This tool can be installed on Windows, Mac, Unix, or any other machine that has Python 3 and pip installed. If you do not have Python 3 or pip installed, you can download them from the official Python website: https://www.python.org/downloads/. Once you have installed Python 3 and pip, follow the steps above to install and use the tool.

## Author

This tool was developed by Oleg Vinokurov. You can find him on LinkedIn at [https://www.linkedin.com/in/vinokurov/](https://www.linkedin.com/in/vinokurov/).

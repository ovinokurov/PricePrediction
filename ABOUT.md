The Cryptocurrency Price Prediction Tool is a machine learning-based application that predicts the price of a cryptocurrency over a selected time period. The tool retrieves historical price data from the CryptoCompare API, trains a linear regression model on that data, and generates price predictions for the selected time period.

The tool is written in Python and uses several libraries and APIs to achieve its functionality. The Requests library is used to make HTTP requests to the CryptoCompare API, while OpenPyXL is used to create and modify Excel spreadsheets. Scikit-learn is used to train and use the machine learning model, and Colorama is used to add color to the console output.

To use the tool, the user is prompted to select a cryptocurrency and time period to analyze. The tool then retrieves historical price data from the CryptoCompare API and trains a linear regression model on the data. The model is used to generate price predictions for the selected time period, which are written to an Excel spreadsheet and saved in the "reports" folder.

Installation:

To install the Cryptocurrency Price Prediction Tool, follow these steps:

Clone the repository: ** git clone https://github.com/ovinokurov/PricePrediction.git **
Install the required libraries: ** pip install requests openpyxl scikit-learn colorama **
Run the tool: ** python main.py **
The tool can be installed on Windows, Mac, Unix, or any other machine that supports Python.

The main.py file is the entry point of the tool. It contains the main program loop and handles user input. When the tool is run, the main program loop begins by prompting the user to select a cryptocurrency and time period to analyze. It then retrieves historical price data from the CryptoCompare API, trains a linear regression model on the data, and generates price predictions for the selected time period.

The CryptoCompare API is used to retrieve historical price data for the selected cryptocurrency. The API endpoint is defined as ** https://min-api.cryptocompare.com/data/v2/histohour **. The tool makes HTTP requests to this endpoint to retrieve the historical price data. The API parameters used to retrieve the data are defined based on the user's selected time period.

Once the historical price data is retrieved, it is processed and prepared for machine learning. The timestamps and prices are extracted from the data and used to train a linear regression model using the Scikit-learn library. The trained model is then used to generate price predictions for the selected time period.

The price predictions are written to an Excel spreadsheet using the OpenPyXL library. The spreadsheet is saved in the "reports" folder with a filename that includes the name of the selected cryptocurrency, the selected time period, and the current date and time.

The Colorama library is used to add color to the console output. This makes the output more readable and visually appealing. Green text is used to indicate successful operations, while red text is used to indicate errors.

In summary, the Cryptocurrency Price Prediction Tool is a machine learning-based application that uses historical price data from the CryptoCompare API to predict the price of a cryptocurrency over a selected time period. The tool is written in Python and uses several libraries and APIs to achieve its functionality. It can be installed on Windows, Mac, Unix, or any other machine that supports Python. The main program loop handles user input and retrieves historical price data from the CryptoCompare API. The data is processed and prepared for machine learning using the Scikit-learn library. The trained model is then used to generate price predictions for the selected time period, which are written to an Excel spreadsheet using the OpenPyXL library. The tool provides users with valuable insights into the future price movements of a selected cryptocurrency, which can be used to make informed investment decisions.
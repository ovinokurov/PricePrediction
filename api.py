from flask import Flask, jsonify, request
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
from flask_caching import Cache
import time
import pickle
import json

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


# Define function to fetch price data from the API
@cache.cached(timeout=60 * 60)
def fetch_price_data(crypto):
    api_endpoint = f'https://api.coingecko.com/api/v3/coins/{crypto.lower()}/market_chart?vs_currency=usd&days=3652'
    response = requests.get(api_endpoint)
    price_data = response.json()
    prices = pd.DataFrame(price_data['prices'], columns=['timestamp', 'price'])
    prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
    return prices

# Define function to train a linear regression model on price data
def train_model(prices):
    # Convert timestamps to Unix timestamp integers
    timestamps = prices['timestamp'].map(lambda x: int(x.timestamp()))

    # Train a linear regression model on the price data
    model = LinearRegression()
    model.fit(timestamps.to_frame(), prices['price'])

    return model

@app.route('/predictions/<freq>/<int:period>/<crypto>', methods=['GET'])
def get_predictions(freq, period, crypto):
    # Validate user input
    if freq not in ['hour', 'day', 'month', 'year']:
        return jsonify({'error': 'Invalid frequency specified. Please use "hour", "day", "month", or "year".'}), 400

    if period < 1 or period > 3652:
        return jsonify({'error': 'Invalid period specified. Please use a value between 1 and 3652.'}), 400

    cache_key = f'{crypto}-{freq}-{period}'
    cached_predictions = cache.get(cache_key)
    if cached_predictions is not None:
        return jsonify(cached_predictions)
    
    # Fetch and aggregate price data
    prices = fetch_price_data(crypto)

    # Train a linear regression model on the price data
    model = train_model(prices)

    # Predict future prices using the trained model
    if freq == 'hour':
        future_dates = pd.date_range(start=prices['timestamp'].iloc[-1], periods=period, freq='H')
    elif freq == 'day':
        future_dates = pd.date_range(start=prices['timestamp'].iloc[-1], periods=period, freq='D')
    elif freq == 'month':
        future_dates = pd.date_range(start=prices['timestamp'].iloc[-1], periods=period, freq='M')
    else:
        future_dates = pd.date_range(start=prices['timestamp'].iloc[-1], periods=period, freq='Y')
    
    future_dates_int = future_dates.map(lambda x: int(x.timestamp()))
    future_dates_reshaped = future_dates_int.to_numpy().reshape(-1, 1)
    future_prices = model.predict(future_dates_reshaped)

    # Format the predictions based on the frequency requested
    if freq == 'hour':
        predictions = [{'date': date.strftime('%Y-%m-%d %H:%M:%S'), 'price': str(price)} for date, price in zip(future_dates, future_prices)]
    elif freq == 'day':
        predictions = [{'date': date.strftime('%Y-%m-%d'), 'price': str(price)} for date, price in zip(future_dates, future_prices)]
    elif freq == 'month':
        predictions = [{'date': date.strftime('%Y-%m'), 'price': str(price)} for date, price in zip(future_dates, future_prices)]
    else:
        predictions = [{'date': date.strftime('%Y'), 'price': str(price)} for date, price in zip(future_dates, future_prices)]

    cache.set(cache_key, predictions, timeout=60 * 60)
    
    return jsonify(predictions)

# View the cache contents
@app.route('/cache', methods=['GET'])
def view_cache():
    cache_data = []
    json_cache_data = []
    for key, value in cache.cache._cache.items():
        try:
            deserialized_value = pickle.loads(value[1])
        except (pickle.UnpicklingError, TypeError):
            try:
                json_str = value[1].decode('utf-8')
                deserialized_value = json.loads(json_str)
            except (json.JSONDecodeError, TypeError):
                deserialized_value = value[1].decode('utf-8', 'ignore')

        expiration_time = value[0] - time.monotonic() if value[0] != 0 else None
        cache_data.append({'key': key, 'value': deserialized_value, 'expiration_time': expiration_time})

        json_cache_data = json.dumps(cache_data, default=str)


    return jsonify(json_cache_data)

if __name__ == '__main__':
    app.run(debug=True)
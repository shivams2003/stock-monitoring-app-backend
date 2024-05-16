import requests

FINNHUB_QUOTE_URL = 'https://finnhub.io/api/v1/quote'
FINNHUB_PROFILE_URL = 'https://finnhub.io/api/v1/stock/profile2'
API_KEY = 'cp2s0cpr01qoj4h1g78gcp2s0cpr01qoj4h1g790'  # Replace with your Finnhub API key

def get_stock_data(symbol):
    params = {
        'symbol': symbol,
        'token': API_KEY
    }
    response = requests.get(FINNHUB_QUOTE_URL, params=params)
    data = response.json()
    if 'c' in data:
        return {
            'symbol': symbol,
            'price': data['c']
        }
    return None

def get_company_profile(symbol):
    params = {
        'symbol': symbol,
        'token': API_KEY
    }
    response = requests.get(FINNHUB_PROFILE_URL, params=params)
    data = response.json()
    if 'name' in data:
        return {
            'symbol': symbol,
            'name': data['name'],
            'exchange': data['exchange'],
            'industry': data['finnhubIndustry']
        }
    return None

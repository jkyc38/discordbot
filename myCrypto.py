from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os



KEY = os.environ['KEY']

def coin_id(symbol):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
    'symbol':symbol,
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': KEY,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    #pprint.pprint(json.loads(response.text))
    coin_id = json.loads(response.text)['data'][0]['id']
    return str(coin_id)
def coin(name, symbol):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {
    'slug':name,
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': KEY,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    price =json.loads(response.text)['data'][coin_id(symbol)]['quote']['USD']['price']
    percent_change = json.loads(response.text)['data'][coin_id(symbol)]['quote']['USD']['percent_change_1h']
    return [price, percent_change]
def coin_tweet(name, symbol):
    rounded_price = str(round(coin(name, symbol)[0],3))
    rounded_percent = str(round(coin(name, symbol)[1],2))
    return f"The price of ${name} is {rounded_price} and it changed by {rounded_percent}% at this hour. "


def test(symbol):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
    parameters = {
    'symbol':symbol,
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': KEY,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    #pprint.pprint(json.loads(response.text))
    coin_data = json.loads(response.text)['data'][0]
    return coin_data
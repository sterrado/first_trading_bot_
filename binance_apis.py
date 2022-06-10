from binance import Client
from binance.exceptions import BinanceAPIException
from database import save_trade
from datetime import datetime
from decimal import Decimal, ROUND_HALF_DOWN
from secrets import api_key, api_secret

# binance apis


client = Client(api_key, api_secret)

base_endpoint = "https://testnet.binancefuture.com"


def get_eth_price():
    avg_price = client.get_avg_price(symbol='ETHUSDT')
    return avg_price['price']


def get_eth_balance():
    balance = client.get_asset_balance(asset='ETH')
    return balance


def get_usdt_balance():
    balance = client.get_asset_balance(asset='USDT')
    return balance


def buy_market_order(quantity):
    eth_price = round(float(get_eth_price()))
    quantity = float(quantity) / eth_price
    quantity = '%.3f' % float(quantity)
    quantity = float(quantity) - 0.001
    order = client.order_market_buy(
        symbol='ETHUSDT',
        quantity=quantity)
    # guardar en la DB
    save_trade({'executed_at': str(datetime.now()), 'quantity': quantity,
               'market_price': eth_price, 'succesful': True, 'market_order_buy': True})
    return True


def sell_market_order(quantity):
    quantity = '%.3f' % Decimal(quantity)
    quantity = float(quantity) - float(0.001)
    order = client.order_market_sell(
        symbol='ETHUSDT',
        quantity=quantity)
    # guardar en la DB
    eth_price = round(float(get_eth_price()), 2)
    save_trade({'executed_at': str(datetime.now()), 'quantity': quantity,
               'market_price': eth_price, 'succesful': True, 'market_order_buy': False})
    return True

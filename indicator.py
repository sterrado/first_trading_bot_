import requests
from models import Current_MA_Request, Last_MA_Request
from time import sleep


APIKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNhbnRpYWdvdGVycmFkb0BnbWFpbC5jb20iLCJpYXQiOjE2NDk0NDAxNTksImV4cCI6Nzk1NjY0MDE1OX0.a_jnKuHLh_gJh-Z8lpfcJerm_NDXkeXBnGXinmnru_c"


def get_current_MA_value(request:  Current_MA_Request):
    MA_VALUE = requests.get("https://api.taapi.io/ma?secret="+request["secret"] +
                            "&exchange=binance&symbol="+request["symbol"]+"&interval="+request["interval"]).json()
    return MA_VALUE


def get_last_MA_value(request:  Last_MA_Request):
    MA_VALUE = requests.get("https://api.taapi.io/ma?secret="+request["secret"] +
                            "&exchange=binance&symbol="+request["symbol"]+"&interval="+request["interval"]+"&backtrack="+request["backtrack"]).json()
    return MA_VALUE


def analyze_tendency():
    current_ma_value = get_current_MA_value(
        {"secret": APIKey, "symbol": "ETH/USDT", "interval": "1d"})
    sleep(16)
    last_ma_value = get_last_MA_value(
        {"secret": APIKey, "symbol": "ETH/USDT", "interval": "1d", "backtrack": "1"})
    current_ma_value = float(current_ma_value['value'])
    last_ma_value = float(last_ma_value['value'])
    if (current_ma_value >= last_ma_value):
        tendencia_positiva = True
    elif (current_ma_value < last_ma_value):
        tendencia_positiva = False
    else:
        raise ValueError("algo salio mal con el indicador")
    return tendencia_positiva

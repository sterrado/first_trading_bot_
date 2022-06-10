from pydantic import BaseModel, Field
from datetime import datetime
import uuid

# modelos


class Trade(BaseModel):
    executed_at: str = Field(default=datetime.now())
    market_price: float
    quantity: float
    succesful: bool
    market_order_buy: bool

    def __str__(self):
        return self.id

# indicadores


class Current_MA_Request(BaseModel):
    secret: str = Field(...)
    exchange: str = 'binance'
    symbol: str = Field(...)
    interval: str = Field(...)


class Last_MA_Request(Current_MA_Request):
    backtrack: str = Field(...)

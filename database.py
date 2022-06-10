from models import Trade
import pymongo
import random
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017/")


database = client.bot_trades
collection = database.trades


def save_trade(trade: Trade):
    document = trade
    result = collection.insert_one(document)
    return document


def fetch_one_trade(trade_id: str):
    document = collection.find_one({"_id": ObjectId(trade_id)})
    return document


def fetch_all_trades():
    trades = []
    cursor = collection.find({})
    for document in cursor:
        trades.append(Trade(**document))
    return trades

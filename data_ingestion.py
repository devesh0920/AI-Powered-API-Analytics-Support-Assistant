from pymongo import MongoClient

def fetch_api_logs():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["api_db"]
    collection = db["logs"]
    
    data = list(collection.find())
    return data
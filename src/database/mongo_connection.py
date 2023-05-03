import os
from database.mongo_client import MongoMetricsClient

def build_mongo_uri(username, password, host, port, db) -> str:
    return f"mongodb://{username}:{password}@{host}:{port}/{db}"


username = "root"
password = "12345678"

host = "localhost"
if os.getenv("ENVIRONMENT") is not None and os.getenv("ENVIRONMENT") == "production":
    redis_host = "mongo-service"

db_name = "metrics"
port = 27017

mongo_uri: str = build_mongo_uri(username, password, host, port, db_name)

mongo_client = MongoMetricsClient(mongo_uri)

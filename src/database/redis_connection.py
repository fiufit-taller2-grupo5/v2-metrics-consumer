from redis import Redis
import os

redis_port = 6379

redis_host = "localhost"
if os.getenv("ENVIRONMENT") is not None and os.getenv("ENVIRONMENT") == "production":
    redis_host = "redis-service"


redis_connection = Redis(host=redis_host, port=redis_port, db=0)


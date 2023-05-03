import redis

class RedisClient:

    def __init__(self, redis: redis.Redis):
        self.client = redis


    def get_all_from_list(self, key: str):
        return self.client.lrange(key, 0, -1)
    

    def remove_all_from_list(self, key: str):
        self.client.delete(key)
        
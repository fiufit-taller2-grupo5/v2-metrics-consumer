from typing import List
import redis

class RedisClient:

    def __init__(self, redis: redis.Redis):
        self.client = redis


    def get_all_from_list(self, key: str) -> List[str]:
        redis_list = self.client.lrange(key, 0, -1)
        json_list = [elem.decode('utf-8') for elem in redis_list]
        return json_list
    

    def remove_all_from_list(self, key: str):
        self.client.delete(key)
        
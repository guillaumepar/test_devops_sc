import os
import redis


class CacheClient:
    def __init__(self):
        self.client = redis.StrictRedis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=0)
    
    def get(self, key: str):
        return self.client.get(key)
    
    def set(self, key: str, value: str):
        return self.client.set(key, value)
    
    def exists(self, key: str):
        return self.client.exists(key)
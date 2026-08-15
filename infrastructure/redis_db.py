import redis.asyncio as redis
from constants import REDIS_HOST, REDIS_PORT

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT
)

def get_redis_client():
    return redis_client

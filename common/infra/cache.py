import redis

redis_client = redis.StrictRedis(host="cache", port=6379, decode_responses=True)

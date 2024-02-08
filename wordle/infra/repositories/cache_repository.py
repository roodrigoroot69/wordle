from typing import Any
from dataclasses import dataclass

from wordle.domain.repositories.cache_interface import ICacheRepository


EXPIRATION_TIME = 300

@dataclass
class RedisCacheRepository(ICacheRepository):

    redis_client: object

    def save_attempt(self, key: str, value: Any):
        self.redis_client.set(key, value, EXPIRATION_TIME)

    def get_attempt(self, key: str) -> str:
        return self.redis_client.get(key) or 1

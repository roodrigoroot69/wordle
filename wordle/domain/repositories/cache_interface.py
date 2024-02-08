from abc import ABC, abstractmethod
from typing import Any

class ICacheRepository(ABC):

    @abstractmethod
    def save_attempt(self, key: str, value: Any):
        raise NotImplementedError

    @abstractmethod
    def get_attempt(self, key: str):
        raise NotImplementedError
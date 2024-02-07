from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class IWordsRepository(ABC):

    @abstractmethod
    def get_active_word(self):
        raise NotImplementedError

    @abstractmethod
    def get_word(self):
        raise NotImplementedError

    @abstractmethod
    def deactivate_word(self, word: str):
        raise NotImplementedError

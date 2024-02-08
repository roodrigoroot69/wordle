from abc import ABC, abstractmethod
from typing import Dict

class IWinnersRepository(ABC):

    @abstractmethod
    def save_winner(self, user_id: int, word: str):
        raise NotImplementedError

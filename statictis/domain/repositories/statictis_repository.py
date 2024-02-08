from abc import ABC, abstractmethod


class IStatictisRepository(ABC):

    @abstractmethod
    def get_most_accurate_words(self):
        raise NotImplementedError

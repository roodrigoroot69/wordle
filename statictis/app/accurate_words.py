from dataclasses import dataclass
from typing import List

from statictis.domain.repositories.statictis_repository import IStatictisRepository


@dataclass
class AccurateWordsProcessor:
    statictis_repository: IStatictisRepository

    def execute(self) -> List:
        return self.statictis_repository.get_most_accurate_words()

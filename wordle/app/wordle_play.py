import threading
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from fastapi import HTTPException

from wordle.domain.repositories.word_interface import IWordsRepository
from wordle.domain.repositories.cache_interface import ICacheRepository
from wordle.domain.repositories.winners_repository import IWinnersRepository


ATTEMPTS_ALLOWED = 6


@dataclass
class WordlePlayProcessor:
    word: str
    user: Dict
    word_repository: IWordsRepository
    cache_repository: ICacheRepository
    winner_repository: IWinnersRepository
    validated_letters: Optional[List[Dict]] = field(default_factory=list)

    def execute(self) -> List[Dict]:
        self._validate_attempts()
        self._validate_length_user_world(self.word)

        current_word = self.word_repository.get_active_word().word
        self._valdiate_each_letter(current_word)

        current_attempts = self.cache_repository.get_attempt(self.user["username"])
        self.cache_repository.save_attempt(
            self.user["username"], int(current_attempts) + 1
        )

        self._is_user_wins()

        return self.validated_letters

    def _validate_length_user_world(self, word: str):
        if not len(word) == 5:
            raise HTTPException(
                status_code=400, detail="La palabra debe ser de 5 letras"
            )

    def _valdiate_each_letter(self, current_word):
        for index, letter in enumerate(self.word):
            if self._is_the_same_letter(index, current_word):
                self._save_punctuation(letter, 1)

            elif self._is_letter_inside_word(letter, current_word):
                self._save_punctuation(letter, 2)

            else:
                self._save_punctuation(letter, 3)

    def _is_the_same_letter(self, index: int, current_word):
        return self.word[index] == current_word[index]

    def _is_letter_inside_word(self, letter: str, word: str):
        return letter in word

    def _is_user_wins(self):
        total_score = sum(letters["value"] for letters in self.validated_letters)
        if total_score == 5:
            self.winner_repository.save_winner(
                user_id=self.user["user_id"],
                word=self.word,
            )

    def _save_punctuation(self, letter: str, value: int):
        self.validated_letters.append({"letter": letter, "value": value})

    def _validate_attempts(self):
        attemps = self.cache_repository.get_attempt(self.user["username"])
        if attemps and int(attemps) == ATTEMPTS_ALLOWED:
            raise HTTPException(
                status_code=400,
                detail="Has alcanzado el límite de intentos permitidos.",
            )

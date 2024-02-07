from dataclasses import dataclass, field
from typing import Dict, List, Optional

from fastapi import HTTPException

from wordle.domain.repositories.word_interface import IWordsRepository

@dataclass
class WordlePlayProcessor:
    word_repository: IWordsRepository
    word: str
    user: Dict
    validated_letters: Optional[List[Dict] ]= field(default_factory=list)

    def execute(self) -> List[Dict]:
        self._validate_length_user_world(self.word)

        current_word = self.word_repository.get_active_word().word

        self._valdiate_each_letter(current_word)

        return self.validated_letters

    def _validate_length_user_world(self, word: str):
        if not len(word) == 5:
            raise HTTPException(status_code=400, detail="La palabra debe ser de 5 letras")

    def _valdiate_each_letter(self, current_word):
        for index, letter in enumerate(self.word):
            if self._is_the_same_letter(index, current_word):
                self._save_punctuation(letter, 1)

            elif self._is_letter_inside_word(letter, current_word):
                self._save_punctuation(letter, 2)

            else:
                self._save_punctuation(letter, 3)

    def _save_punctuation(self, letter: str, value: int):
        self.validated_letters.append({
            "letter": letter,
            "value": value
        })

    def _is_the_same_letter(self, index: int, current_word):
        return self.word[index] == current_word[index]

    def _is_letter_inside_word(self, letter: str, word: str):
        return letter in word

    def user_wins(self):
        total_score = (letters['value'] for letters in self.validated_letters)
        if total_score == 5:
            print("user wins")
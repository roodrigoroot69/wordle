from typing import List


import sys
import os

# Obtén la ruta del directorio common
common_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(common_path)

from common.infra.database import SessionLocal
from common.infra.models import Words

session = SessionLocal()
# Lee el archivo y realiza inserciones por lotes
batch_size = 5000  # Número de palabras a insertar por lote


def save_word(word: str, words_batch: List):
    if word:
        words_batch.append({'word': word})

        if len(words_batch) >= batch_size:
            session.bulk_insert_mappings(Words, words_batch)
            session.commit()
            words_batch = []

with open('words.txt', 'r', encoding='utf-8') as file:
    words_batch = []
    for line in file:
        print(".", end="")
        try:
            word = line.strip()
            save_word(word=word, words_batch=words_batch)
        except UnicodeDecodeError:
            if "-" in word:
                word = word.replace("-", "")
            save_word(word, words_batch)
    # Inserta las palabras restantes si quedan en el último lote
    if words_batch:
        session.bulk_insert_mappings(Words, words_batch)
        session.commit()

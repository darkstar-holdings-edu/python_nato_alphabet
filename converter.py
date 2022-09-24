import pandas as pd  # type: ignore
import re

DATA_FILE = "nato_phonetic_alphabet.csv"


class NATO:
    translation_key: dict[str, str]

    def __init__(self) -> None:
        df = pd.read_csv(DATA_FILE)
        self.translation_key = {row.letter: row.code for (index, row) in df.iterrows()}

    def convert(self, data: str) -> list[list[str]]:
        parsed_data = re.sub(" +", " ", data).strip().upper()  # Clean up text

        converted_data = []

        for word in parsed_data.split(" "):
            letters = [letter for letter in word]
            converted_data.append(
                [
                    self.translation_key[letter]
                    for letter in letters
                    if letter in self.translation_key
                ]
            )

        return converted_data

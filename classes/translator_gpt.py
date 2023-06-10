import openai

from lib.config import API_KEY, SYSTEM_ROLE, USER_ROLE
from classes._db import db


class TranslatorGPT:

    def __init__(self) -> None:
        self.translated_data: dict = {}
        openai.api_key = API_KEY

    def translate_item(self, key, value, max_attemps=10, retry_delay=5):
        attemps = 0
        while attemps < max_attemps:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': SYSTEM_ROLE},
                    {'role': 'user', 'content': USER_ROLE + str(value)}
                ],
                temperature=0.2
            )

            translation = response.choices[0].message.content.strip()

            self.translated_data[key] = translation
            self._insert_translated_data()
            return translation

    def _insert_translated_data(self):
        for key, value in self.translated_data.items():
            db.execute(f"""
                INSERT INTO translation
                (key, value)
                VALUES
                ("{key}", "{value}")
            """)
        self.translated_data.clear()

    def _get_translated_data(self):
        result = db.query("""
            SELECT key, value
            FROM translations
        """)
        return result

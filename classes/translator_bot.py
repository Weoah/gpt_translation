import openai
import json

from lib.config import API_KEY, SYSTEM_ROLE, USER_ROLE


class TranslatorGPT:

    def __init__(self) -> None:
        self.json_data: dict = {}
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
            print(translation)

            self.translated_data[key] = translation
            self._save_translated_data()
            return translation

    def _save_translated_data(self):
        with open('translated_data.json', 'w', encoding='utf-8') as f:
            json.dump(self.translated_data, f, ensure_ascii=False, indent=4)

    def _load_translated_data(self):
        try:
            with open('translated_data.json', 'r', encoding='utf-8') as f:
                self.translated_data = json.load(f)
        except FileNotFoundError:
            self.translated_data = {}

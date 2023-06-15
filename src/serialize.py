import json


class JsonSerialize:

    def __init__(self) -> None:
        self.untranslated_path = 'enGB.json'
        self.translated_path = 'ptGB.json'
        self.temp_path = 'temp.json'

    def load_untranslated_data(self) -> dict:
        try:
            with open(self.untranslated_path, 'r', encoding='utf8') as f:
                result = json.load(f)
            return result
        except FileNotFoundError:
            return {"$id": 1, "strings": []}

    def save_translated_data(self, translated_data: list[dict]) -> None:
        data = self._mount_json_data(translated_data)
        with open(self.temp_path, 'w', encoding="utf8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def _mount_json_data(self, translated_data: list[dict]) -> dict:
        result = {"$id": 1, "strings": translated_data}
        return result


serialize = JsonSerialize()

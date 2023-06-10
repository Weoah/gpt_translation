import json

from classes.translator_gpt import TranslatorGPT
from classes._db import db
# from lib.config import KEY_TEST, VALUE_TEST

translator = TranslatorGPT()


def load_untranslated_data():
    try:
        with open('enGB.json', 'r', encoding='utf8') as f:
            result = json.load(f)
        return result
    except FileNotFoundError:
        return {"$id": 1, "strings": []}


def insert_unstranslated_data(data_dict: dict):
    for key, value in data_dict.items():
        db.execute_diferente("""
            INSERT INTO unstranslated
            (key, value)
            VALUES
            (?, ?)
        """, (key, value))


def get_unstranslated_keys():
    result = db.query("""
        SELECT key, value
        FROM unstranslated
        WHERE key = 'Key'
    """)
    return result


def get_unstranslated_values():
    result = db.query("""
        SELECT key, value
        FROM unstranslated
        WHERE key = 'Value'
    """)
    return result


def mount_json_data(translated_data):
    result = {"$id": 1, "strings": translated_data}
    return result


def save_translated_data(translated_data):
    with open('translated_data_temp.json', 'w', encoding="utf8") as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=4)


def load_translated_data():
    ...


def translate_range(json_data, new_json_data, translated_data):
    ...


def main():
    json_data = load_untranslated_data()
    new_json_data = load_new_json_data()
    translated_data = load_translated_data()
    translate_range(json_data, new_json_data, translated_data)


if __name__ == "__main__":
    ...
    # data_list = load_untranslated_data()['strings']
    # print(len(data_list))
    # for data_dict in data_list:
    #     insert_unstranslated_data(data_dict)

    result1 = get_unstranslated_keys()
    result2 = get_unstranslated_values()

    data: list[dict] = []
    {data.append({key: value, key2: value2})
     for (key, value), (key2, value2) in zip(result1, result2)}

    print(len(data))

    data = mount_json_data(data)
    save_translated_data(data)

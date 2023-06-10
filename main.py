from classes.translator_bot import TranslatorGPT
# from lib.config import KEY_TEST, VALUE_TEST

translator = TranslatorGPT()


def load_json_data_base():
    ...


def load_new_json_data():
    ...


def load_translated_data():
    ...


def translate_range(json_data, new_json_data, translated_data):
    ...


def main():
    json_data = load_json_data_base()
    new_json_data = load_new_json_data()
    translated_data = load_translated_data()
    translate_range(json_data, new_json_data, translated_data)

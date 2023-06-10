from src.translator_gpt import translator
from src.dba import dba
from src.serialize import serialize


class Main:

    def __init__(self) -> None:
        self.untranslated_data: list[dict] = []
        self._get_data()

    def run_translate(self):
        for item in self.untranslated_data:
            translator.translate_one_item(item)
            break

    def _get_data(self) -> None:
        untranslated_keys = dba.get_untranslated_keys()
        untranslated_values = dba.get_untranslated_values()
        for (key, keys), (value, values) \
                in zip(untranslated_keys, untranslated_values):
            self.untranslated_data.append({key: keys, value: values})

    def _insert_untranslated_data(self):
        data_list = serialize.load_untranslated_data()['strings']
        for dict_item in data_list:
            dba.insert_untranslated_data(dict_item)


if __name__ == "__main__":
    main = Main()

    main.run_translate()

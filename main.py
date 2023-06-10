# from classes.translator_gpt import translator
from classes.dba import dba
from classes.serialize import serialize


def translate_one_item(dict_):
    print(dict_)
    if not dba.check_if_translated(dict_['Key']):
        ...


if __name__ == "__main__":
    ...
    # data_list = load_untranslated_data()['strings']
    # print(len(data_list))
    # for data_dict in data_list:
    #     insert_unstranslated_data(data_dict)

    result1 = dba.get_unstranslated_keys()
    result2 = dba.get_unstranslated_values()

    data: list[dict] = []
    {data.append({key: value, key2: value2})  # type: ignore
     for (key, value), (key2, value2) in zip(result1, result2)}

    # print(len(data))

    # data = mount_json_data(data)
    serialize.save_translated_data(data)

    for data_item in data:
        translate_one_item(data_item)
        break

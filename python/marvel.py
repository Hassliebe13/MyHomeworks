from dataset.marvel import full_dict
from pprint import pprint

"""
    Конвернтер строки в число
    :param input_value: строка
    :return: число или None
"""


def str_to_int_or_none(input_value: str) -> int | None:
    if input_value.isdigit():
        return int(input_value)
    else:
        return None


"""
    Функция запроса чисел у пользователя
    :return: список чисел и None
"""


def user_input_id() -> list[int | None]:
    return list(map(str_to_int_or_none, input("Введите цифры через пробел: ").split()))


def main():
    """
    Вызывает user_input_id() для получения списка ID, введенных пользователем.
    Фильтрует full_dict на основе введенных пользователем ID и создает новый словарь list_dict_filter_marvel.
    """
    list_user_id = user_input_id()
    list_dict_filter_marvel = dict(
        filter(lambda x: x[0] in list_user_id, full_dict.items())
    )
    pprint(list_dict_filter_marvel)
    """
    Фильтрует режиссеров из full_dict.
    """
    set_director = set(value["director"] for key, value in full_dict.items())
    pprint(set_director)
    """
    Создает копию full_dict, преобразуя значение 'year' в строку для каждой записи.
    """
    copy_full_dict = {
        key: {**value, "year": str(value["year"])} for key, value in full_dict.items()
    }
    pprint(copy_full_dict)
    """
    marvel_filter_title_ch, который содержит только те элементы из full_dict, 
    у которых название фильма начинается с буквы "Ч" (заглавной).
    """
    marvel_filter_title_ch = dict(
        filter(
            lambda x: x[1]["title"][0].strip() == "Ч",
            filter(lambda x: x[1]["title"] is not None, full_dict.items()),
        )
    )
    pprint(marvel_filter_title_ch)


if __name__ == "__main__":
    main()

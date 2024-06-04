from src.masks import mask_by_account, mask_by_card

import re

def number_encryption(account_type: str) -> str:
    """
    Функция, которая будет уметь работать как с картами, так и со счетами.
    Принимать на вход строку с информацией — тип карты/счета и номер карты/счета.
    Возвращать исходную строку с замаскированным номером карты/счета
    """
    if len(account_type) == 0:
        raise ValueError("Неверный номер")

    number_account = account_type.split()[-1]
    name_account = " ".join(account_type.split()[0:-1])

    if len(number_account) == 16:
        number = mask_by_card(number_account)
    elif len(number_account) == 20:
        number = mask_by_account(number_account)
    else:
        number = "Введите правильный номер"

    return f"{name_account} {number}"


def return_date(date: str) -> str:
    """
    Функция, которая принимает на вход строку вида 2018-07-11T02:26:18.671407
    и возвращает строку с датой в виде 11.07.2018
    """
    pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$"
    if len(date) == 26 and re.match(pattern, date):
        return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    elif len(date) == 0:
        return "Пустая строка"
    else:
        return "Ошибка ввода"

# if __name__ == '__main__':
#     account_type = "Visa 2452245136547895"
#     print(number_encryption(account_type))
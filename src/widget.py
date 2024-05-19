from src.masks import mask_by_account, mask_by_card


def number_encryption(account_type: str) -> str:
    """
    Функция, которая будет уметь работать как с картами, так и со счетами.
    Принимать на вход строку с информацией — тип карты/счета и номер карты/счета.
    Возвращать исходную строку с замаскированным номером карты/счета
    """
    number_account = account_type.split()[-1]
    name_account = " ".join(account_type.split()[0:-1])

    if len(number_account) == 16:
        number = mask_by_card(number_account)
    elif len(number_account) == 20:
        number = mask_by_account(number_account)
    else:
        number = "Введите правильный номер"

    return f"{name_account} {number}"


if __name__ == '__main__':
    account_type = "Visa Classic 2452245136547895"
    print(number_encryption(account_type))

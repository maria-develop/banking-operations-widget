def mask_by_card(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    if card_number.isdigit() and len(card_number) == 16:
        mask_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        return mask_number
    else:
        return "Введите правильный номер"


# card_number = "Visa 2452245136547895"
# print(mask_by_card(card_number))


def mask_by_account(personal_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if personal_account.isdigit() and len(personal_account) == 20:
        mask_account = "**" + personal_account[-4:]
        return mask_account
    else:
        return "Введите правильный номер"


# personal_account = "24525245173654378952"
# print(mask_by_account(personal_account))

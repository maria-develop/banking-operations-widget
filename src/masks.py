import logging
import os

from config import LOGS_DIR

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)

# Определяем путь к лог-файлу в корне проекта
# log_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
# if not os.path.exists(LOGS_DIR):
#     os.makedirs(LOGS_DIR)
log_file = os.path.join(LOGS_DIR, "masks.log")
print(log_file)


file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(messege)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_by_card(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    if card_number.isdigit() and len(card_number) == 16:
        mask_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        logger.info(f"Маскировка номера карты: {card_number} -> {mask_number}")
        return mask_number
    else:
        logger.error(f"Некорректный номер карты: {card_number}")
        return "Введите правильный номер"


# card_number = "Visa 2452245136547895"
# print(mask_by_card(card_number))


def mask_by_account(personal_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if personal_account.isdigit() and len(personal_account) == 20:
        mask_account = "**" + personal_account[-4:]
        logger.info(f"Маскированный номер счета:{personal_account}  -> {mask_account}")
        return mask_account
    else:
        logger.error(f"Некорректный номер счета: {personal_account}")
        return "Введите правильный номер"


# personal_account = "24525245173654378952"
# print(mask_by_account(personal_account))

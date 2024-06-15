import json
import os
from typing import Union

import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)

# Определяем путь к лог-файлу в корне проекта
log_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)
log_file = os.path.join(log_directory, "utils.log")
print(log_file)


file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(messege)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_list_operations(path: str) -> Union[list, dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""

    try:
        logger.info(f"Открываем файл {path}")
        with open(path, "r", encoding="utf-8") as operations_file:
            try:
                operations_data = json.load(operations_file)
                if isinstance(operations_data, (list, dict)):
                    logger.info(f"Файл {path} успешно прочитан и содержит допустимые данные.")
                    return operations_data
                else:
                    logger.warning(f"Файл {path} не содержит список или словарь.")
                    return []
            except json.JSONDecodeError:
                logger.error(f"Ошибка декодирования JSON в файле {path}.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}.")
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при обработке файла {path}: {e}")
        return []


# if __name__ == '__main__':
#     print(get_list_operations("C:/Users/User/Desktop/python_rpoject_Maria/DZ_9.2_/data/operations.json"))


# if __name__ == '__main__':
#     Печать текущего рабочего каталога для отладки
#     print(f"Текущий рабочий каталог: {os.getcwd()}")

    # Используйте абсолютный путь
    # abs_path = os.path.abspath("data/operations.json")
    # print(f"Абсолютный путь к файлу: {abs_path}")

    # Проверка пути к файлу
    # if os.path.exists(abs_path):
    #     print("Файл найден")
    # else:
    #     print("Файл не найден")
    #
    # print(get_list_operations(abs_path))

import json
from typing import Union


def get_list_operations(path: str) -> Union[list, dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""

    try:
        with open(path, "r", encoding="utf-8") as operations_file:
            try:
                operations_data = json.load(operations_file)
                if isinstance(operations_data, (list, dict)):
                    return operations_data
                else:
                    print("Файл не содержит список или словарь")
                    return []
            except json.JSONDecodeError:
                print("Ошибка декодирования JSON")
                return []
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return []
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return []


if __name__ == '__main__':
    print(get_list_operations("../data/operations.json"))

# if __name__ == '__main__':
#     Печать текущего рабочего каталога для отладки
    # print(f"Текущий рабочий каталог: {os.getcwd()}")
    #
    # Используйте абсолютный путь
    # abs_path = os.path.abspath("data/operations.json")
    # print(f"Абсолютный путь к файлу: {abs_path}")
    #
    # Проверка пути к файлу
    # if os.path.exists(abs_path):
    #     print("Файл найден")
    # else:
    #     print("Файл не найден")
    #
    # print(get_list_operations(abs_path))

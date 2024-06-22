from src.utils import get_list_operations
from src.import_csv_xlsx import read_transactions, read_transactions_xlsx
from src.processing import filter_by_state, sorted_by_date
from src.transaction_filter import filter_transactions_by_description
from src.external_api import convert_transaction_amount
from src.widget import number_encryption, return_date

import os
import re


DATA_DIR = 'data'
JSON_FILE = os.path.join(DATA_DIR, 'operations.json')
CSV_FILE = os.path.join(DATA_DIR, 'transactions.csv')
XLSX_FILE = os.path.join(DATA_DIR, 'transactions_excel.xlsx')


def main():
    """Реализует основную логику проекта и связывает функциональности между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == '1':
        file_type = 'JSON'
        transactions = get_list_operations(JSON_FILE)
    elif choice == '2':
        file_type = 'CSV'
        transactions = read_transactions(CSV_FILE)
    elif choice == '3':
        file_type = 'XLSX'
        transactions = read_transactions_xlsx(XLSX_FILE)
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
        return

    print(f"Для обработки выбран {file_type}-файл.")

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = input("Пользователь: ").upper()

        if state in {"EXECUTED", "CANCELED", "PENDING"}:
            # Добавим отладочную информацию
            # for i, txn in enumerate(transactions):
            #     if 'state' not in txn:
            #         print(f"Транзакция {i} не содержит ключ 'state': {txn}")
            filtered_transactions = filter_by_state(transactions, state)  # в транзакции передается список словарей
            print(f"Операции отфильтрованы по статусу \"{state}\"")
            break
        else:
            print(f"Статус операции \"{state}\" недоступен.")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Отсортировать операции по дате? Да/Нет")
    sort_choice = input("Пользователь: ").lower()

    if sort_choice == 'да':
        print("Отсортировать по возрастанию или по убыванию?")
        sort_order = input("Пользователь: ").lower()
        ascending = sort_order == 'по возрастанию'
        filtered_transactions = sorted_by_date(filtered_transactions, ascending)

    print("Выводить только рублевые транзакции? Да/Нет")
    ruble_choice = input("Пользователь: ").lower()

    if ruble_choice == 'да':
        filtered_transactions = [
            txn for txn in filtered_transactions
            if txn["operationAmount"]["currency"]["code"] == "RUB"
            or convert_transaction_amount(txn) != txn["operationAmount"]["amount"]
        ]

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    desc_choice = input("Пользователь: ").lower()

    if desc_choice == 'да':
        search_string = input("Введите строку поиска: ")
        text_input = re.compile(r"\d+|\D+")
        if text_input is not search_string:
            return "Без фильтра по ключевому слову"
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")
    for txn in filtered_transactions:
        # Добавлена отладочная печать
        if "from" not in txn or "to" not in txn:
            print(f"Отсутствуют ключи 'from' или 'to' в транзакции: {txn}")
        date = return_date(txn["date"])
        description = txn["description"]
        from_account = number_encryption(txn["from"]) if "from" in txn else "N/A"
        to_account = number_encryption(txn["to"]) if "to" in txn else "N/A"
        # from_account = number_encryption(txn.get("from", "N/A"))
        # to_account = number_encryption(txn.get("to", "N/A"))
        # from_account = number_encryption(txn["from"])
        # to_account = number_encryption(txn["to"])
        amount = txn["operationAmount"]["amount"]
        currency = txn["operationAmount"]["currency"]["name"]
        print(f"{date} {description}")
        print(f"{from_account} -> {to_account}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == '__main__':
    main()

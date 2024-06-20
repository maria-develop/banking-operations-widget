import csv
import logging
import os

import pandas as pd

from config import LOGS_DIR

# from openpyxl import load_workbook


logger = logging.getLogger("csv_xlsx")
logger.setLevel(logging.INFO)


log_file = os.path.join(LOGS_DIR, "csv_xlsx.log")
print(log_file)


file_handler = logging.FileHandler(log_file)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(messege)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions(file_path: str) -> list[dict]:
    """Читает файл CSV и возвращает список словарей с транзакциями."""
    transactions = []
    try:
        logger.info(f"Открываем файл {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            header = next(reader)
            for row in reader:
                row_dict = {
                    "id": row[header.index("id")],
                    "state": row[header.index("state")],
                    "date": row[header.index("date")],
                    "operationAmount": {
                        "amount": row[header.index("amount")],
                        "currency": {
                            "name": row[header.index("currency_name")],
                            "code": row[header.index("currency_code")],
                        },
                    },
                    "description": row[header.index("description")],
                    "from": row[header.index("from")],
                    "to": row[header.index("to")],
                }
                transactions.append(row_dict)
        return transactions

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}.")
        return [{}]
    except Exception as e:
        logger.error(f"Неожиданная ошибка при обработке файла {file_path}: {e}")
        return [{}]


def read_transactions_xlsx(file_path: str) -> list[dict]:
    """Читает файл Excel и возвращает список словарей с транзакциями."""
    try:
        # Попробуем открыть файл напрямую с помощью openpyxl
        # wb = load_workbook(filename=file_path)
        print("Файл успешно открыт с помощью openpyxl")
        # Если файл открывается, попробуем загрузить его в pandas DataFrame
        df = pd.read_excel(file_path, engine='openpyxl')
        print("Файл успешно открыт и прочитан с помощью pandas")
        transactions_x = df.apply(
            lambda row: {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
                "description": row["description"],
                "from": row["from"] if pd.notna(row["from"]) else "",
                "to": row["to"] if pd.notna(row["to"]) else "",
            },
            axis=1,
        ).tolist()
        return transactions_x

    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}.")
        return [{}]
    except Exception as e:
        logger.error(f"Неожиданная ошибка при обработке файла {file_path}: {e}")
        return [{}]


# def read_transactions_xlsx(file_path: str) -> list[dict]:
#     """Читает файл Excel и возвращает список словарей с транзакциями. Форма без operationAmount"""
#     transactions_x = []
#     try:
#         df = pd.read_excel(file_path)
#         transactions = df.to_dict(orient='records')
#     except FileNotFoundError:
#         print(f"Файл не найден: {file_path}")
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#     return transactions


# def read_transactions(file_path: str) -> list[dict]:
#     """Читает файл CSV и возвращает список словарей с транзакциями. Форма без operationAmount"""
#     transactions = []
#     try:
#         with open(file_path, newline='', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(csvfile, delimiter=';')
#             for row in reader:
#                 transactions.append(row)
#     except FileNotFoundError:
#         logger.error(f"Файл не найден: {file_path}.")
#         return [{}]
#     except Exception as e:
#         logger.error(f"Неожиданная ошибка при обработке файла {file_path}: {e}")
#         return [{}]
    # return transactions


# if __name__ == '__main__':
    # result = read_transactions("C:/Users/User/Desktop/python_rpoject_Maria/DZ_9.2_/data/transactions.csv")
    # res_x = read_transactions_xlsx("C:/Users/User/Desktop/python_rpoject_Maria/DZ_9.2_/data/transactions_excel.xlsx")
    # print(result)
    # print(res_x)

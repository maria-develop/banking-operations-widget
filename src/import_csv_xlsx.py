import csv
import pandas as pd


def read_transactions(file_path: str) -> list[dict]:
    """Читает файл CSV и возвращает список словарей с транзакциями."""
    transactions = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            header = next(reader)
            # transactions = []
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
        print(f"Файл не найден: {file_path}")
        return [{}]
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return [{}]


# def read_transactions(file_path: str) -> list[dict]:
#     """Читает файл CSV и возвращает список словарей с транзакциями. Форма без operationAmount"""
#     transactions = []
#     try:
#         with open(file_path, newline='', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(csvfile, delimiter=';')
#             for row in reader:
#                 transactions.append(row)
#     except FileNotFoundError:
#         print(f"Файл не найден: {file_path}")
#         return [{}]
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
#         return [{}]
    # return transactions



if __name__ == '__main__':
    result = read_transactions("C:/Users/User/Desktop/python_rpoject_Maria/DZ_9.2_/data/transactions.csv")
    print(result)

import re
# from typing import List, Dict
from collections import Counter


def filter_transactions_by_description(transactions: list[dict], search_string: str) -> list[dict]:
    """Фильтрует список транзакций по строке поиска в описании."""
    pattern = re.compile(search_string, re.IGNORECASE)
    filtered_transactions = [
        transaction for transaction in transactions
        if pattern.search(transaction.get("description", ""))
    ]
    return filtered_transactions


def count_transactions_by_category(transactions: list[dict], categories: list[str]) -> dict[str, int]:
    """Считает количество транзакций в каждой категории."""
    # category_count = {category: 0 for category in categories}
    category_count: Counter[str] = Counter()

    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category in description:
                category_count[category] += 1
                break

    return dict(category_count)


if __name__ == "__main__":
    transactions = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "operationAmount": {
                "amount": "16210",
                "currency": {
                    "name": "Sol",
                    "code": "PEN",
                },
            },
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "operationAmount": {
                "amount": "29740",
                "currency": {
                    "name": "Peso",
                    "code": "COP",
                },
            },
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
        },
        # ... другие транзакции
    ]

    search_string = "Перевод с карты"
    filtered_transactions = filter_transactions_by_description(transactions, search_string)
    print(filtered_transactions)

    categories = ["Перевод организации", "Перевод с карты на карту", "Открытие вклада"]
    category_count = count_transactions_by_category(transactions, categories)
    print(category_count)

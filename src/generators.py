from typing import Any


def filter_by_currency(transactions: list[dict[str, dict]], currency: str) -> Any:
    """Функция принимает список словарей с банковскими операциями
    и возвращает итератор, который выдает по очереди операции,
    в которых указана заданная валюта."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("name") == currency:
            yield transaction


# usd_transactions = filter_by_currency(transactions, "USD")
#
# for _ in range(2):
#     print(next(usd_transactions)["id"])


def transaction_descriptions(transactions: list[dict[str, dict]]) -> Any:
    """Генератор, который принимает список словарей и
    возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description")


# descriptions = transaction_descriptions(transactions)
#
# for _ in range(5):
#     print(next(descriptions))


def card_number_generator(start: int, end: int) -> Any:
    """Генератор номеров банковских карт, который должен генерировать номера карт
    в формате XXXX XXXX XXXX XXXX, где X — цифра"""

    for num in range(start, end + 1):
        yield "{:04d} {:04d} {:04d} {:04d}".format(
            (num // 10**12) % 10**4, (num // 10**8) % 10**4, (num // 10**4) % 10**4, num % 10**4
        )


# for card_number in card_number_generator(1, 5):
#     print(card_number)

import unittest

from src.transaction_filter import count_transactions_by_category, filter_transactions_by_description


class TestFilterTransactionsByDescription(unittest.TestCase):
    def test_filter_transactions_by_description(self):
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
        ]

        search_string = "Перевод с карты"
        expected = [
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
        ]

        result = filter_transactions_by_description(transactions, search_string)
        self.assertEqual(result, expected)


class TestCountTransactionsByCategory(unittest.TestCase):
    def test_count_transactions_by_category(self):
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
        ]

        categories = ["Перевод организации", "Перевод с карты на карту", "Открытие вклада"]
        expected = {
            "Перевод организации": 1,
            "Перевод с карты на карту": 1,
            "Открытие вклада": 0,
        }

        result = count_transactions_by_category(transactions, categories)
        self.assertEqual(result, expected)

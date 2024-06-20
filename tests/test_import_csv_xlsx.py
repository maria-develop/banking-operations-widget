from unittest.mock import mock_open, patch

# Импортируем функцию для чтения транзакций
from src.import_csv_xlsx import read_transactions, read_transactions_xlsx

# Тесты для read_transactions
csv_data = """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организ
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discov 3172601889670065;Discov 0720428384694643;Перевод с карты"""


def test_read_transactions():
    """Тестирует чтение корректного CSV-файла."""
    with patch("builtins.open", mock_open(read_data=csv_data)):
        # Ожидаемый результат
        expected = [
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
                "description": "Перевод организ",
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
                "description": "Перевод с карты",
                "from": "Discov 3172601889670065",
                "to": "Discov 0720428384694643",
            },
        ]

        # Вызов функции и проверка результата
        result = read_transactions("data/transactions.csv")
        assert result == expected


def test_file_not_found():
    """Тестирует случай, когда файл не найден"""
    with patch("builtins.open", side_effect=FileNotFoundError("Файл не найден")):
        result = read_transactions("data/non_existent_file.csv")
        assert result == [{}]


def test_general_exception():
    """Тестирует общий случай ошибки при чтении файла"""
    with patch("builtins.open", side_effect=Exception("Некоторая ошибка")):
        result = read_transactions("data/corrupt_file.csv")
        assert result == [{}]


def test_file_not_found_xlsx():
    """Тестирует случай, когда файл не найден"""
    with patch("builtins.open", side_effect=FileNotFoundError("Файл не найден")):
        result = read_transactions_xlsx("data/non_existent_file.xlsx")
        assert result == [{}]


def test_general_exception_xlsx():
    """Тестирует общий случай ошибки при чтении файла"""
    with patch("builtins.open", side_effect=Exception("Некоторая ошибка")):
        result = read_transactions_xlsx("data/corrupt_file.xlsx")
        assert result == [{}]

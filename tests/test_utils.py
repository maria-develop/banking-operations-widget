import json
from unittest.mock import patch

from src.utils import get_list_operations

import unittest


class TestGetListOperations(unittest.TestCase):

    @patch("builtins.open")
    def test_file_not_found(self, mock_open):
        """Проверяет, что функция возвращает пустой список операций в случае, если файл не найден"""
        mock_open.side_effect = FileNotFoundError
        result = get_list_operations("nonexistent_file.json")
        self.assertEqual(result, [])

    @patch("builtins.open")
    def test_unexpected_error(self, mock_open):
        """Проверяет, что функция возвращает пустой список операций в случае возникновения неожиданной ошибки"""
        mock_open.side_effect = Exception("Some unexpected error")
        result = get_list_operations("some_file.json")
        self.assertEqual(result, [])






# Тест на успешное чтение транзакций из файла
@patch('builtins.open')
@patch('os.path.exists')
def test_read_transactions(mock_exists, mock_open):
    # Mock os.path.exists to return True
    mock_exists.return_value = True

    # Mock open function to return a JSON string
    mock_open.return_value.__enter__.return_value.read.return_value = '[{"id": 207126257, "state": "EXECUTED"}]'

    path = '../data/operations.json'
    transactions = get_list_operations(path)

    assert transactions == [{"id": 207126257, "state": "EXECUTED"}]
    mock_exists.assert_called_once_with(path)
    mock_open.assert_called_once_with(path, 'r', encoding='utf-8')

# Тест на случай, когда файл содержит не список
@patch('builtins.open')
@patch('os.path.exists')
def test_read_transactions_not_a_list(mock_exists, mock_open):
    mock_exists.return_value = True
    mock_open.return_value.__enter__.return_value.read.return_value = '{}'

    file_path = 'data/operations.json'
    transactions = read_data_from_json(file_path)

    assert transactions == {}
    mock_exists.assert_called_once_with(file_path)
    mock_open.assert_called_once_with(file_path, 'r', encoding='utf-8')

# Тест на случай, когда файл пустой
@patch('builtins.open')
@patch('os.path.exists')
def test_read_transactions_empty_file(mock_exists, mock_open):
    mock_exists.return_value = True
    mock_open.return_value.__enter__.return_value.read.return_value = ''

    file_path = 'data/operations.json'
    transactions = read_data_from_json(file_path)

    assert transactions == []
    mock_exists.assert_called_once_with(file_path)
    mock_open.assert_called_once_with(file_path, 'r', encoding='utf-8')

# Тест на случай, когда файл не найден
@patch('os.path.exists')
def test_read_transactions_file_not_found(mock_exists):
    mock_exists.return_value = False

    file_path = 'data/operations.json'
    transactions = read_data_from_json(file_path)

    assert transactions == []
    mock_exists.assert_called_once_with(file_path)

# Запуск тестов
if __name__ == "__main__":
    test_read_transactions()
    test_read_transactions_not_a_list()
    test_read_transactions_empty_file()
    test_read_transactions_file_not_found()
    print("Все тесты пройдены успешно!")
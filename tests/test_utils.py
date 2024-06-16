import json
import unittest
from unittest.mock import mock_open, patch

from src.utils import get_list_operations


@patch("builtins.open", new_callable=mock_open,
       read_data=json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]))
def test_get_list_operations_valid_list(mock_file):
    """Тестирует функцию с корректным JSON файлом, содержащим список"""
    result = get_list_operations("dummy_path")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["amount"] == 200


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"id": 1, "amount": 100}))
def test_get_list_operations_valid_dict(mock_file):
    """Тестирует функцию с корректным JSON файлом, содержащим словарь"""
    result = get_list_operations("dummy_path")
    assert isinstance(result, dict)
    assert result["id"] == 1
    assert result["amount"] == 100


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_get_list_operations_empty_file(mock_file):
    """Тестирует функцию с пустым файлом"""
    result = get_list_operations("dummy_path")
    assert isinstance(result, list)
    assert len(result) == 0


@patch("builtins.open", new_callable=mock_open, read_data="{invalid json}")
def test_get_list_operations_invalid_json(mock_file):
    """Тестирует функцию с файлом, содержащим некорректный JSON"""
    result = get_list_operations("dummy_path")
    assert isinstance(result, list)
    assert len(result) == 0


@patch("builtins.open", side_effect=FileNotFoundError)
def test_get_list_operations_file_not_found(mock_file):
    """Тестирует функцию с отсутствующим файлом"""
    result = get_list_operations("dummy_path")
    assert isinstance(result, list)
    assert len(result) == 0


@patch("builtins.open", side_effect=Exception("Unexpected error"))
def test_get_list_operations_unexpected_error(mock_file):
    """Тестирует функцию с неожиданной ошибкой при открытии файла"""
    result = get_list_operations("dummy_path")
    assert isinstance(result, list)
    assert len(result) == 0


if __name__ == '__main__':
    unittest.main()

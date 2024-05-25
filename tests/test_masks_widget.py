import pytest
from src.widget import number_encryption


@pytest.fixture
def account_type():
    return "Visa Classic 2452245136547895"


@pytest.mark.parametrize(
    "account_type, expected",
    [("Visa Classic 2452245136547895", "Visa Classic 2452 45** **** 7895"),
     ("Счет 24522451365478951234", "Счет **1234"),
     ("Счет 24522451365478951287134", "Счет Введите правильный номер"),
     ("", "Неверный номер"), ],
)
def test_number_encryption(account_type, expected):
    assert number_encryption(account_type) == expected

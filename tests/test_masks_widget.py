import pytest

from src.widget import number_encryption, return_date


@pytest.fixture
def account_type():
    return "Visa Classic 2452245136547895"


@pytest.mark.parametrize(
    "account_type, expected",
    [
        ("Visa Classic 2452245136547895", "Visa Classic 2452 45** **** 7895"),
        ("Счет 24522451365478951234", "Счет **1234"),
        ("Счет 24522451365478951287134", "Счет Введите правильный номер"),
    ],
)
def test_number_encryption(account_type, expected):
    assert number_encryption(account_type) == expected


def test_number_encryption_error():
    with pytest.raises(ValueError):
        number_encryption("")


@pytest.fixture
def date():
    return "2018-07-11T02:26:18.671407"


@pytest.mark.parametrize(
    "date, expect",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-11T02:26:18.671407", "11.07.2019"),
        ("2019-07-11T02:26:18.671407022", "Ошибка ввода"),
        ("", "Пустая строка"),
    ],
)
def test_return_date(date, expect):
    assert return_date(date) == expect

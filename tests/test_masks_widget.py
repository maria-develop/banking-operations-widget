import pytest

from src.masks import mask_by_account, mask_by_card
from src.widget import number_encryption, return_date


@pytest.fixture
def account_type():
    return "Visa Classic 2452245136547895"


@pytest.mark.parametrize(
    "account_type, expected",
    [
        ("Visa Classic 2452245136547895", "Visa Classic 2452 24** **** 7895"),
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
        ("2018-07-11", "Ошибка ввода"),
        ("abcd-ef-ghTij:kl:mn.opqrst", "Ошибка ввода"),
        ("", "Пустая строка"),
    ],
)
def test_return_date(date, expect):
    assert return_date(date) == expect


@pytest.fixture
def card_number():
    return "2452245136547895"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("2452245136547895", "2452 24** **** 7895"),
        ("245224513654789525", "Введите правильный номер"),
        ("", "Введите правильный номер"),
    ],
)
def test_mask_by_card_valid(card_number, expected):
    assert mask_by_card(card_number) == expected


def test_mask_by_card_non_digit():
    card_number = "1234abcd89012345"
    expected_response = "Введите правильный номер"
    assert mask_by_card(card_number) == expected_response


@pytest.fixture
def personal_account():
    return "24522451365478952569"


@pytest.mark.parametrize(
    "personal_account, expected",
    [
        ("2452245136547895", "Введите правильный номер"),
        ("245224513654789525", "Введите правильный номер"),
        ("24522451365478952569", "**2569"),
    ],
)
def test_mask_by_account(personal_account, expected):
    assert mask_by_account(personal_account) == expected


def test_mask_by_account_non_digit():
    personal_account = "1234567890123456789a"
    expected_response = "Введите правильный номер"
    assert mask_by_account(personal_account) == expected_response

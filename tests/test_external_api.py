import unittest
from unittest.mock import Mock, patch

# import requests
from src.external_api import convert_transaction_amount, get_api, get_exchange_rate


# Тесты для get_api
@patch("requests.get")
def test_get_api_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": True}
    mock_get.return_value = mock_response

    url = "http://dummy_url.com"
    params = {"key": "value"}
    headers = {"Authorization": "Bearer token"}

    response = get_api(url, params, headers)
    assert response.json() == {"success": True}


# Тесты для get_exchange_rate
@patch("requests.request")
def test_get_exchange_rate_success(mock_request):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 74.85}
    mock_request.return_value = mock_response

    amount = 100
    from_currency = "USD"
    to_currency = "RUB"
    result = get_exchange_rate(amount, from_currency, to_currency)
    assert result == 74.85


# Тесты для convert_transaction_amount
def test_convert_transaction_amount_rub():
    transaction = {
        "operationAmount": {
            "amount": 3000,
            "currency": {
                "code": "RUB"
            }
        }
    }
    result = convert_transaction_amount(transaction)
    assert result == 3000.0


if __name__ == '__main__':
    unittest.main()

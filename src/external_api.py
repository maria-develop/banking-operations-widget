import os
from typing import Any, Dict, Optional

import requests
from dotenv import load_dotenv
from requests import Response

# Загрузка переменных окружения из файла .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"


def get_api(url: str, params: dict[str, str | float], headers: Optional[Dict[str, Any]]) -> Response:
    """Обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли"""
    response = requests.get(url, params=params, headers=headers)

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Полученный ответ от сервера не является корректным HTTP-ответом
        response = requests.get(BASE_URL, timeout=5)  # запрос не получил ответа в течение заданного времени
        response = requests.get(BASE_URL, allow_redirects=False)  # кол-во перенаправлений превышает max доп. значение
    except requests.exceptions.HTTPError:
        print("HTTP Error. Please check the URL.")
    except requests.exceptions.ConnectionError:
        print("Connection Error. Please check your network connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Please check your internet connection.")
    except requests.exceptions.TooManyRedirects:
        print("Too many redirects. Please check the URL.")
    except requests.exceptions.RequestException:
        print("An error occurred. Please try again later.")

    return response


def get_exchange_rate(amount: float, from_currency: str, to_currency: str = "RUB") -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

    headers = {
        "apikey": API_KEY
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()
    if data.get("result") is None:
        print("Ошибка выгрузки api")
        return 0.0
    return float(data.get("result"))


def convert_transaction_amount(transaction: dict) -> float | Any:
    """Функция для обработки транзакции"""
    try:
        amount = transaction["operationAmount"]["amount"]
        from_currency = transaction["operationAmount"]["currency"]["code"]
        if from_currency != "RUB":
            return get_exchange_rate(amount, from_currency)
        return float(amount)
    except KeyError as e:
        raise KeyError(f"Key {e} not found in JSON data.")


# if __name__ == '__main__':
    # print(get_exchange_rate(52000, "USD", "RUB"))
    # print(convert_transaction_amount({
    #     "id": 441945886,
    #     "state": "EXECUTED",
    #     "date": "2019-08-26T10:50:58.294041",
    #     "operationAmount": {
    #       "amount": "31957.58",
    #       "currency": {
    #         "name": "руб.",
    #         "code": "RUB"
    #       }}}))
    # print(convert_transaction_amount({
    #     "id": 41428829,
    #     "state": "EXECUTED",
    #     "date": "2019-07-03T18:35:29.512364",
    #     "operationAmount": {
    #         "amount": "822.37",
    #         "currency": {
    #             "name": "USD",
    #             "code": "USD"
    #         }
    #     }}))

import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    :param transaction: словарь с транзакцией
    :return: сумма в рублях
    """
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))

    if currency_code == "RUB":
        return amount

    if currency_code not in {"USD", "EUR"} or not API_KEY:
        return 0.0

    params = {"from": currency_code, "to": "RUB", "amount": amount}

    headers = {"apikey": API_KEY}

    response = requests.get(API_URL, params=params, headers=headers)
    response.raise_for_status()
    result = response.json()
    return float(result.get("result", 0))

import os
from typing import Optional

from dotenv import load_dotenv
from utils import read_json_file
from external_api import convert_to_rub
from generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)
from decorators import log


load_dotenv()


@log("main.log")
def mask_account_number(account_number: str) -> str:
    """Маскирует номер счета, оставляя только последние 4 цифры"""
    if not account_number:
        raise ValueError("Account number is empty")
    return "**" + account_number[-4:]


@log("main.log")
def sort_transactions_by_date(transactions: list[dict]) -> list[dict]:
    """Сортирует транзакции по дате"""
    return sorted(transactions, key=lambda x: x.get("date", ""))


@log("main.log")
def display_transaction_info(json_path: str, currency: str = "USD") -> None:
    """
    Загружает данные из JSON, фильтрует по валюте, конвертирует сумму в рубли и выводит информацию.
    """
    transactions = read_json_file(json_path)

    if not transactions:
        print("Файл пуст, не найден или содержит некорректные данные.")
        return

    sorted_tx = sort_transactions_by_date(transactions)
    filtered = filter_by_currency(sorted_tx, currency)

    print(f"\n🔎 Транзакции в валюте {currency}:")
    for tx in filtered:
        tx_id = tx.get("id")
        desc = tx.get("description", "Без описания")
        try:
            amount_rub = convert_to_rub(tx)
            print(f"#{tx_id}: {desc} — {amount_rub:.2f} RUB")
        except Exception as e:
            print(f"Ошибка при конвертации транзакции #{tx_id}: {e}")


@log()
def demo_card_generation(start: int = 1, end: int = 3) -> None:
    print("\n🎴 Генерация номеров карт:")
    for card in card_number_generator(start, end):
        print(card)


if __name__ == "__main__":
    path_to_data: str = "data/operations.json"

    if not os.getenv("EXCHANGE_API_KEY"):
        print("❌ Не найден EXCHANGE_API_KEY в .env. Проверьте конфигурацию.")
    else:
        print("📁 Обработка операций из JSON-файла...\n")
        display_transaction_info(path_to_data, currency="USD")

    demo_card_generation()

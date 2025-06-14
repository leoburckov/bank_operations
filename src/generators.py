def filter_by_currency(transactions, currency_code):
    """Генератор для фильтрации транзакций по валюте."""
    for tx in transactions:
        if tx.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield tx


def transaction_descriptions(transactions):
    """Генератор для получения описания транзакций."""
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start, end):
    """Генератор номеров карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, end + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:16]

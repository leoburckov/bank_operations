import pytest
from src.analytics import process_bank_search, process_bank_operations

data = [
    {"description": "Оплата мобильной связи"},
    {"description": "Перевод со счета на счет"},
    {"description": "Открытие вклада"},
    {"description": "Оплата мобильной связи"},
    {"description": "Покупка в магазине"},
]

def test_process_bank_search_case_insensitive():
    result = process_bank_search(data, "оплата")
    assert len(result) == 2
    assert all("оплата".lower() in tx["description"].lower() for tx in result)

def test_process_bank_search_no_match():
    result = process_bank_search(data, "налоги")
    assert result == []

def test_process_bank_operations_count():
    categories = ["Оплата мобильной связи", "Открытие вклада"]
    result = process_bank_operations(data, categories)
    assert result == {
        "Оплата мобильной связи": 2,
        "Открытие вклада": 1
    }

def test_process_bank_operations_empty():
    categories = ["Налоги"]
    result = process_bank_operations(data, categories)
    assert result == {}

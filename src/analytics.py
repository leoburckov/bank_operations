import re
from collections import Counter
from typing import Dict, List


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Возвращает список операций, в которых description содержит подстроку search (поиск регистронезависимый).
    :param data: список транзакций
    :param search: строка для поиска в описании
    :return: отфильтрованный список транзакций
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [tx for tx in data if pattern.search(tx.get("description", ""))]


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям из description, используя Counter.
    :param data: список транзакций
    :param categories: список категорий (названий операций)
    :return: словарь {"категория": количество}
    """
    descriptions = [tx.get("description", "") for tx in data if tx.get("description") in categories]
    return dict(Counter(descriptions))


def normalize_status(value: str) -> str:
    """
    Приводит статус к верхнему регистру для унификации.
    """
    return value.strip().upper()

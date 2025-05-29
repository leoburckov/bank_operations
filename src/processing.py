from typing import List, Dict, Any

"""operations_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
] пример ввода данных"""


def filter_by_state(operations_list: List[Dict[str, Any]], state: str = "EXECUTED") -> list[Dict[str, Any]]:
    """ "Функция сортировки по ключу state"""

    return [item for item in operations_list if item.get("state") == state]


def sort_by_date(operations_list: List[Dict[str, Any]]) -> list[Dict[str, Any]]:
    """Функция сортировки даты"""
    return sorted(operations_list, key=lambda item: item["date"], reverse=True)

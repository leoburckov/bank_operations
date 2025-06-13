from typing import Dict, List

data_bank = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(data_bank: List[dict]) -> List[dict]:
    """Возвращает новый список словарей, содержащих только те записи, у которых значение ключа 'state' равно
    'EXECUTED'."""

    new_list = [pay for pay in data_bank if pay.get("state") == "EXECUTED"]
    return new_list


filtered_data = filter_by_state(data_bank)
# print(filtered_data)
print("----------Filtered Data----------------")
for i in range(len(filtered_data)):
    print(filtered_data[i])


def sort_by_date(data_bank: List[Dict], descending: bool = True) -> List[Dict]:
    """принимает список словарей и возвращает отсортированный по дате"""

    return sorted(data_bank, key=lambda x: x["date"], reverse=descending)


sorted_data = sort_by_date(data_bank)
print("----------Sorted Data----------------")
for i in range(len(sorted_data)):
    print(sorted_data[i])

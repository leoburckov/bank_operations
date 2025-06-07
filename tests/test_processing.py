import pytest
from typing import Dict, List
from src.processing import filter_by_state, sort_by_date


@pytest.fixture(scope="module")
def test_data() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]


@pytest.mark.parametrize(
    "input_data, expected_result",
    [
        ([{"id": 1, "state": "EXECUTED"}], ["EXECUTED"]),
        ([{"id": 1, "state": "PENDING"}], []),
        ([{"id": 1, "state": "EXECUTED"},
          {"id": 2, "state": "EXECUTED"},
          {"id": 3, "state": "CANCELED"}
          ],
         ["EXECUTED", "EXECUTED"]
         ),
        ([], [])
    ]
)
def test_filter_by_state(input_data: List[Dict], expected_result: List[Dict]) -> None:
    result = filter_by_state(input_data)
    assert len(result) == len(expected_result)
    for item in result:
        assert item['state'] in expected_result


@pytest.mark.parametrize(
    "input_data, descending, expected_order",
    [
        # Проверяем порядок по возрастанию
        ([{"date": "2020-01-01T00:00:00Z"},
          {"date": "2019-01-01T00:00:00Z"},
          {"date": "2021-01-01T00:00:00Z"}
          ],
         False,
         ["2019-01-01T00:00:00Z", "2020-01-01T00:00:00Z", "2021-01-01T00:00:00Z"]
         ),
        # Проверяем порядок по убыванию
        ([{"date": "2020-01-01T00:00:00Z"},
          {"date": "2019-01-01T00:00:00Z"},
          {"date": "2021-01-01T00:00:00Z"}
          ],
         True,
         ["2021-01-01T00:00:00Z", "2020-01-01T00:00:00Z", "2019-01-01T00:00:00Z"]
         ),
        # Проверяем случай с одинаковыми датами
        ([{"date": "2020-01-01T00:00:00Z"},
          {"date": "2020-01-01T00:00:00Z"},
          {"date": "2021-01-01T00:00:00Z"}
          ],
         True,
         ["2021-01-01T00:00:00Z", "2020-01-01T00:00:00Z", "2020-01-01T00:00:00Z"]
         )
    ]
)
def test_sort_by_date(input_data: List[Dict], descending: bool, expected_order: bool) -> None:
    result = sort_by_date(input_data, descending)
    actual_dates = [item['date'] for item in result]
    assert actual_dates == expected_order
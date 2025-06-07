from typing import Union,List

import pytest

from src.masks import get_date, get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_exception",
    [
        ("1234123412341234", None),
        ("12341234", ValueError),
        ("", ValueError),
        ("123412341234123X", ValueError),
        ("ABCDEF1234567890", ValueError),
    ],
)


def test_get_mask_card_number(card_number: str, expected_exception: Union[type(ValueError), None]) -> None: # was type[ValueError]
    if expected_exception is None:
        result = get_mask_card_number(card_number)
        assert isinstance(result, str)
    else:
        with pytest.raises(expected_exception):
            get_mask_card_number(card_number)


@pytest.mark.parametrize("card_mask,expected_output",
                         [
                             ("12341234123412345555", None),
                             ("12341234", ValueError),
                             ("", ValueError),
                             ("123412341234123X1111", ValueError),
                             ("ABCDEF12345678901111", ValueError),
                         ],
                         )
def test_get_mask_account(card_mask: str, expected_output: Union[type(ValueError), None]) -> None: # was type[ValueError]
    if expected_output is None:
        get_mask_account(card_mask)
    else:
        with pytest.raises(expected_output):
            get_mask_account(card_mask)


def test_get_date() -> None:
    date = '2024-03-11T02:26:18.671407'
    result = get_date(date)
    assert result == '11.03.2024', "Результат должен быть '11.03.2024'"


@pytest.fixture
def valid_dates() -> List[str]:   # was list[str]
    return [
            '2024-03-11T02:26:18.671407',
            '2000-01-01T00:00:00.000000'
    ]


@pytest.fixture
def invalid_dates()-> List[str]:  # was list[str]
    return [
        '',
        'invalid-date-format',
        '2024-03-11T02:26:18.67140',
        '2024-03-11T02:26:18.6714077'
    ]


def test_get_date_with_valid_dates(valid_dates: List) -> None:   # was list
    for date in valid_dates:
        result = get_date(date)
        assert isinstance(result, str), "Результат должен быть строкой."
        assert len(result.split('.')) == 3, "Результат должен содержать три части."


def test_get_date_with_invalid_dates(invalid_dates: List) -> None: # was list
    for date in invalid_dates:
        with pytest.raises(ValueError):
            get_date(date)
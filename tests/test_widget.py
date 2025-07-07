import pytest

from src.widget import get_date, get_mask_account_card


@pytest.mark.parametrize(
    "card_mask, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account_card(card_mask: str, expected: str) -> None:
    actual = get_mask_account_card(card_mask)
    assert actual == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    actual = get_date(date)
    assert actual == expected

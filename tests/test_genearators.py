import pytest
from generators import filter_by_currency,transaction_descriptions,card_number_generator


# ----------------
# Фикстура: список транзакций
# ----------------
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "date": "2024-05-01T10:00:00",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Payment in USD",
        },
        {
            "id": 2,
            "date": "2024-05-02T11:00:00",
            "operationAmount": {
                "amount": "200",
                "currency": {"name": "EUR", "code": "EUR"},
            },
            "description": "Payment in EUR",
        },
        {
            "id": 3,
            "date": "2024-05-03T12:00:00",
            "operationAmount": {
                "amount": "300",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Another USD payment",
        },
    ]

# ----------------
# Тесты для filter_by_currency
# ----------------
@pytest.mark.parametrize("currency_code,expected_count", [
    ("USD", 2),
    ("EUR", 1),
    ("RUB", 0),
])
def test_filter_by_currency(sample_transactions, currency_code, expected_count):
    result = list(filter_by_currency(sample_transactions, currency_code))
    assert len(result) == expected_count
    for tx in result:
        assert tx["operationAmount"]["currency"]["code"] == currency_code

# ----------------
# Тесты для transaction_descriptions
# ----------------
def test_transaction_descriptions(sample_transactions):
    result = list(transaction_descriptions(sample_transactions))
    expected = [
        "Payment in USD",
        "Payment in EUR",
        "Another USD payment"
    ]
    assert result == expected

# ----------------
# Тесты для card_number_generator
# ----------------
@pytest.mark.parametrize("start,end,expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
])
def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected

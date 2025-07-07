from external_api import convert_to_rub
from unittest.mock import patch


@patch("external_api.requests.get")
def test_convert_to_rub_usd(mock_get) -> None:
    mock_get.return_value.json.return_value = {"result": 97.0}
    mock_get.return_value.raise_for_status = lambda: None

    transaction = {"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}

    result = convert_to_rub(transaction)
    assert result == 97.0


@patch("external_api.requests.get")
def test_convert_to_rub_eur(mock_get) -> None:
    mock_get.return_value.json.return_value = {"result": 105.0}
    mock_get.return_value.raise_for_status = lambda: None

    transaction = {"operationAmount": {"amount": "1", "currency": {"code": "EUR"}}}

    result = convert_to_rub(transaction)
    assert result == 105.0


def test_convert_to_rub_rub() -> None:
    transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}
    assert convert_to_rub(transaction) == 1000.0

from unittest.mock import MagicMock, patch

from src.importers import read_transactions_from_csv, read_transactions_from_excel


@patch("src.importers.pd.read_csv")
def test_read_transactions_from_csv(mock_read_csv):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv("fake_path.csv")

    mock_read_csv.assert_called_once_with("fake_path.csv")
    assert isinstance(result, list)
    assert result == [{"id": 1, "amount": 100}]


@patch("src.importers.pd.read_excel")
def test_read_transactions_from_excel(mock_read_excel):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 2, "amount": 200}]
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel("fake_path.xlsx")

    mock_read_excel.assert_called_once_with("fake_path.xlsx", engine="openpyxl")
    assert isinstance(result, list)
    assert result == [{"id": 2, "amount": 200}]

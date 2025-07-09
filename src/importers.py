from typing import Dict, List

import pandas as pd

csv_data = "data/transactions.csv"
excel_data = "data/transactions_excel.xlsx"


def read_transactions_from_csv(filepath: str) -> List[Dict]:
    """
    Читает CSV-файл и возвращает список транзакций в виде словарей.

    :param filepath: путь к файлу .csv
    :return: список словарей
    """
    df = pd.read_csv(filepath)
    return df.to_dict(orient="records")


def read_transactions_from_excel(filepath: str) -> List[Dict]:
    """
    Читает Excel (.xlsx) файл и возвращает список транзакций в виде словарей.

    :param filepath: путь к .xlsx
    :return: список словарей
    """
    df = pd.read_excel(filepath, engine="openpyxl")
    return df.to_dict(orient="records")

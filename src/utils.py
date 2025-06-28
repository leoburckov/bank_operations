import json
from pathlib import Path
from typing import List, Dict, Any


def read_json_file(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список транзакций.
    :param filepath: путь до JSON-файла
    :return: список транзакций или пустой список
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

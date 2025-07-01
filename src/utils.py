# utils.py
import json
import logging
import os
from typing import Any, Dict, List

# Создание папки logs, если не существует
os.makedirs("logs", exist_ok=True)

# Настройка логгера для utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - utils - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_json_file(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список транзакций.
    :param filepath: путь до JSON-файла
    :return: список транзакций или пустой список
    """
    logger.debug(f"read_json_file started with filepath: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("read_json_file completed successfully — valid list returned")
                return data
            logger.warning("read_json_file returned empty list — JSON is not a list")
            return []
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON format in file: {filepath}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error in read_json_file: {e}")
        return []

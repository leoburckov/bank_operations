# masks.py
import logging
import os

# Создание папки logs, если она не существует
os.makedirs("logs", exist_ok=True)

# Настройка логгера
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - masks - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    logger.debug(f"get_mask_card_number started with input: {card_number}")
    try:
        if len(card_number) != 16 or card_number == "" or not card_number.isdigit():
            raise ValueError("Номер карты должен состоять из 16 цифр")
        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info("get_mask_card_number completed successfully")
        return masked
    except Exception as e:
        logger.error(f"Error in get_mask_card_number: {e}")
        raise


def get_mask_account(card_mask: str) -> str:
    logger.debug(f"get_mask_account started with input: {card_mask}")
    try:
        if len(card_mask) != 20 or card_mask == "" or not card_mask.isdigit():
            raise ValueError("Номер счета должен состоять из 20 цифр")
        masked = f"**{card_mask[-4:]}"
        logger.info("get_mask_account completed successfully")
        return masked
    except Exception as e:
        logger.error(f"Error in get_mask_account: {e}")
        raise


def get_date(date: str) -> str:
    """
    Преобразует дату из формата ISO в формат 'ДД.ММ.ГГГГ'.
    Вход: '2024-06-01T12:34:56.789' → Выход: '01.06.2024'
    """
    logger.debug(f"get_date started with input: {date}")
    try:
        if "T" in date:
            date_part = date.split("T")[0]  # '2024-06-01'
        else:
            date_part = date[:10]  # на случай если без 'T'

        parts = date_part.split("-")  # ['2024', '06', '01']
        if len(parts) != 3:
            raise ValueError("Неправильный формат даты")

        formatted = ".".join(reversed(parts))  # '01.06.2024'
        logger.info("get_date completed successfully")
        return formatted

    except Exception as e:
        logger.error(f"Error in get_date: {e}")
        raise ValueError("Неправильный формат даты")


if __name__ == "__main__":
    try:
        print(get_mask_card_number(input("Введите номер карты: ")))
        print(get_mask_account(input("Введите номер счёта: ")))
        print(get_date(input("Введите дату (в формате ISO с миллисекундами): ")))
    except Exception as e:
        print(f"Ошибка: {e}")

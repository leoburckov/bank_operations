from src.masks import get_mask_account, get_mask_card_number


def get_mask_account_card(card_mask: str) -> str:
    """принимает номер либо номер карты либо счета и возвращает их особенную маску маску"""
    if len(card_mask) == 16:
        return get_mask_card_number(card_mask)
    elif len(card_mask) == 20:
        return get_mask_account(card_mask)
    else:
        # return ""
        raise ValueError(f"Неподходящая длина строки: {len(card_mask)}")


def get_date(date: str) -> str:
    """замена формата даты на краткий дд.мм.гггг"""

    new_date = date[:10].split("-")
    return ".".join(new_date[::-1])


if __name__ == "__main__":
    print(get_mask_account_card(input()))
    print(get_date(input()))

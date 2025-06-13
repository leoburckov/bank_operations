def get_mask_card_number(card_number: str) -> str:
    if len(card_number) != 16 or card_number == "" or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")
    return f"{card_number[:len(card_number) - 12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(card_mask: str) -> str:
    if len(card_mask) != 20 or card_mask == "" or not card_mask.isdigit():
        raise ValueError("Номер счета должен состоять из 20 цифр")
    return f"**{card_mask[-4:]}"


def get_date(date: str) -> str:
    if len(date) != 26 or date == "":
        raise ValueError("Неправильный формат даты")
    else:
        new_date = date[:10].split("-")
    return ".".join(new_date[::-1])


if __name__ == "__main__":
    print(get_mask_card_number(input()))
    print(get_mask_account(input()))
    print(get_date(input()))

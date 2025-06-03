from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_type: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает строку с замаскированным номером"""
    length_name_card_or_account = 0
    for char in number_type:
        if not char.isdigit():
            length_name_card_or_account += 1
    print(len(number_type))
    print(length_name_card_or_account)
    if "Счет" or "счет" in number_type:
        number_mask = get_mask_account(number_type[length_name_card_or_account:])
        return "".join(number_type[0:length_name_card_or_account] + number_mask)
    else:
        number_mask = get_mask_card_number(number_type[length_name_card_or_account:])
        return "".join({number_type[0:length_name_card_or_account] + number_mask})


number_type = input()
print(mask_account_card(number_type))


def get_date(old_data: str) -> str:
    """принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
     и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"
     (
    "11.03.2024"
    )."""
    data = old_data[0:10].split("-")
    return ".".join(data[::-1])


print(get_date("2024-03-11T02:26:18.671407"))

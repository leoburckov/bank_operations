def get_mask_card_number(number_cart: str) -> str:
    """Функция которая принимает на вход номер карты и возвращает ее маску"""
    number_cart = number_cart.replace(" ", "")
    mask_cart = " ".join(number_cart[i : i + 4] for i in range(0, len(number_cart), 4))
    mask_cart_list = list(mask_cart)

    for i in range(len(mask_cart_list)):
        if 7 <= i <= 13 and mask_cart_list[i] != " ":
            mask_cart_list[i] = "*"
    mask_card_number = "".join(mask_cart_list)
    return mask_card_number


mask = get_mask_card_number("1234567812345678")
print(mask)


def get_mask_account(number_cart: str) ->str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    number_cart = number_cart.replace(" ", "")
    number_mask = str(number_cart[-4:])
    return f"**{number_mask}"


print(get_mask_account("123456"))

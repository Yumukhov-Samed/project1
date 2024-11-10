def mask_account_card(number_card: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает маску"""

    str_number_card = str(number_card)
    return f"**{str_number_card[-4:]}"

    """Функция, которая принимает на вход номер карты и возвращает её маску"""

    str_number_card = str(number_card)
    return f"{str_number_card[:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"


def get_date(date: str) -> str:
    """Функция, которая возвращает дату в формате ДД.ММ.ГГГГ."""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"

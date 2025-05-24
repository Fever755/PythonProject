def get_mask_card_number(card_number: str) -> str:
    """Функция возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    # Проверяем, что номер состоит из цифр и имеет правильную длину
    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр.")

    # Формируем маску
    masked_number = f"{card_number[:4]} {card_number[4:6]} ** **** {card_number[12:]}"

    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция возвращает маску номера по правилу
    **** **** **** XXXX"""
    # Проверяем, что номер состоит из цифр и имеет достаточную длину
    if not account_number.isdigit() or len(account_number) < 4:
        raise ValueError(
            "Номер счета должен состоять только из цифр и иметь как минимум 4 цифры."
        )

    # Формируем маску с видимыми последними 4 цифрами
    masked_number = "*" * (len(account_number) - 4) + account_number[-4:]

    return masked_number

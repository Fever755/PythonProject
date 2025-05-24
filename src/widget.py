from masks import get_mask_card_number, get_mask_account

def mask_account_card(data: str) -> str:
    """
    Принимает строку формата:
    - 'Visa Platinum 7000792289606361'
    - 'Maestro 7000792289606361'
    - 'Счет 73654108430135874305'

    Возвращает строку с замаскированным номером карты или счета.
    """
    parts = data.rsplit(" ", 1)  # Делим строку на описание и номер
    if len(parts) != 2:
        raise ValueError("Неверный формат строки. Ожидается: '<тип> <номер>'.")

    prefix, number = parts
    if number.startswith("7") and len(number) == 16:  # Простейшая эвристика для карт
        masked = get_mask_card_number(number)
    elif number.isdigit():
        masked = get_mask_account(number)
    else:
        raise ValueError("Номер должен содержать только цифры.")

    return f"{prefix} {masked}"
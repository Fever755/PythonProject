from datetime import datetime

def filter_by_state(data, state="EXECUTED"):
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data, descending=True):
    """
    Сортирует список словарей по дате (ключ 'date').

    :param data: список словарей с ключом 'date' в формате ISO
    :param descending: True — сортировка по убыванию, False — по возрастанию
    :return: новый отсортированный список словарей
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)
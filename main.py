from src.masks import get_mask_card_number, get_mask_account


def main():
    card_number = '7000792289606361'
    masked_card = get_mask_card_number(card_number)
    print(card_number, '->', masked_card)

    account_number = '73654108430135874305'
    masked_account = get_mask_account(account_number)
    print(account_number, '->', masked_account)


if __name__ == '__main__':
    main()
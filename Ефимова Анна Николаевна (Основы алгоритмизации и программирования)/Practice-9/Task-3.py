
MINTED_COIN_DENOMINATION_25 = 25
MINTED_COIN_DENOMINATION_10 = 10
MINTED_COIN_DENOMINATION_5 = 5
MINTED_COIN_DENOMINATION_1 = 1

Service_price = int(input("Введите стоимость улуги ведьмака: "))

print(f"Для оплаты вам понадобится")

if Service_price//MINTED_COIN_DENOMINATION_25 > 0:
    print(f"{Service_price//MINTED_COIN_DENOMINATION_25} монет(а) с номиналов {MINTED_COIN_DENOMINATION_25}")
    Service_price -= MINTED_COIN_DENOMINATION_25 * (Service_price//MINTED_COIN_DENOMINATION_25)

if Service_price//MINTED_COIN_DENOMINATION_10 > 0:
    print(f"{Service_price//MINTED_COIN_DENOMINATION_10} монет(а) с номиналов {MINTED_COIN_DENOMINATION_10}")
    Service_price -= MINTED_COIN_DENOMINATION_10 * (Service_price//MINTED_COIN_DENOMINATION_10)

if Service_price//MINTED_COIN_DENOMINATION_5 > 0:
    print(f"{Service_price//MINTED_COIN_DENOMINATION_5} монет(а) с номиналов {MINTED_COIN_DENOMINATION_5}")
    Service_price -= MINTED_COIN_DENOMINATION_5 * (Service_price//MINTED_COIN_DENOMINATION_5)

if Service_price//MINTED_COIN_DENOMINATION_1 > 0:
    print(f"{Service_price//MINTED_COIN_DENOMINATION_1} монет(а) с номиналов {MINTED_COIN_DENOMINATION_1}")
    Service_price -= MINTED_COIN_DENOMINATION_1 * (Service_price//MINTED_COIN_DENOMINATION_1)
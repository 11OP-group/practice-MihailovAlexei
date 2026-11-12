
receipt_total = 0

while True:
    price = float(input("Ведите цену товара: "))
    if price < 0:
        print("Ошибука цены. Цена не может быть отрицательной")
    receipt_total += price
    if price == 0:
        break
    

if receipt_total > 1000:
    print("На покупка более 1000 рублей, дается скидка 10%")
    receipt_total = receipt_total * 0.9

print(f"Выдолжны заплатить {receipt_total} рублей")
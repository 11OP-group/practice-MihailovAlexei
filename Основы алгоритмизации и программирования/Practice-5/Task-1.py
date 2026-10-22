
TAX_RATE = 0.13


annual_income = float(input("Введите свой годовой доход: "))

tax = annual_income * TAX_RATE

actual_income = annual_income - tax

print(f"Общая сумма дохода: {annual_income:.2f}")
print(f"Сумма рассчитанного налога: {tax:.2f}")
print(f"Сумма «на руки» после вычета налога: {actual_income:.2f}")




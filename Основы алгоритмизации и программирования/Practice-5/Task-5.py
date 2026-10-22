

capital = int(input("Какую сумму хотите обноличить(целое число, кратное 100): "))

banknotes_5000 = capital//5000
banknotes_2000 = (capital%5000)//2000
banknotes_1000 = ((capital%5000)%2000)//1000
banknotes_500 = (capital%1000)//500
banknotes_100 = (capital%500)//100


print(f"Купюр по 5000р: {banknotes_5000}")
print(f"Купюр по 2000р: {banknotes_2000}")
print(f"Купюр по 1000р: {banknotes_1000}")
print(f"Купюр по 500р: {banknotes_500}")
print(f"Купюр по 100р: {banknotes_100}")
print(f"{capital%100}р невозможно обноличить")


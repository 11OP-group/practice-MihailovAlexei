
m = int(input("Введите стартовое количество организмов: "))
p = int(input("Введите среднесуточное увеличение в процентах: "))
n = int(input("Введите количество дней для размножения: "))

current_population = m

for i in range(1, n+1):
    current_population = current_population*(1+(p/100))
    print(f"День{i} {current_population}")

name = input("Введитие имя: ")

charts = list(name)
antiCharts = charts[::-1]

if charts == antiCharts:
    print("Это палиндром")
else:
    print("Не палиндром")

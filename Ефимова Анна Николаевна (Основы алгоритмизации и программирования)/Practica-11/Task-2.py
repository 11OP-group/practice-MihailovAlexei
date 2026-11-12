BULL = 10
COW = 5
CALF = 0.5

for n in range(11):
    for k in range(20):
        for m in range(201):
            if n*BULL + k*COW + m*CALF == 100:
                   if n+k+m >= 1:
                        print(f"На 100 рублей вы можете купить:{n} быков, {k} коров, {m} телят ")

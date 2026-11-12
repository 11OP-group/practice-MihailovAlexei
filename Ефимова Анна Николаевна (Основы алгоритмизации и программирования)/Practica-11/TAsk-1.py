min_n = 12
num_k = 0
num_m = 0

for n in range(13):
    for k in range(13):
        for m in range(13):
            if 28*n + 30*k + 31*m == 365:
                   if min_n > n:
                        min_n = n
                        num_k = k
                        num_m = m
print(min_n, num_k, num_m)

import random
numders = []

for i in range(10):
    numders.append(random.randint(0, 200))

min_index = numders.index(min(numders))

print(numders)

numders[0], numders[min_index] = numders[min_index], numders[0]

print(numders)

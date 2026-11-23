prices_str = "100 50 200 150 75 300"

prices_list = prices_str.split(' ')

for i in range(0, len(prices_list)):
    prices_list[i] = int(prices_list[i])

prices_list.remove(max(prices_list))

prices_list.append(int(max(prices_list)/2))

print(*prices_list, sep=', ')

print(sum(prices_list)/len(prices_list))
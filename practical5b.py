# Take prices input
prices = tuple(map(int, input("Enter item prices separated by space: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

# b) Cheapest item
print("Cheapest item price:", min(prices))

# c) Costliest item
max_price = max(prices)
print("Costliest item price:", max_price)

# d) Price list in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
count_max = prices.count(max_price)
print("Number of costliest items sold:", count_max)
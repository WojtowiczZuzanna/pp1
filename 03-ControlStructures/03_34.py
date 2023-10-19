amount = int(input("Enter the amount in PLN: "))
coins = [5, 2, 1]
count = 0
for coin in coins:
    while amount >= coin:
        count = count + 1
        amount = amount - coin
print(f"The minimum number of coins required is {count}.")

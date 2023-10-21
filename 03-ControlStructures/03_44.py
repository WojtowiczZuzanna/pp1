list = []

while True:
    x = input("Enter number: ")
    if x == "0":
        break
    list.append(int(x))

quantity = len(list)
sum = sum(list)
mean = sum / quantity

print(f"Quantity = {quantity}, Sum = {sum}, Mean = {mean}")
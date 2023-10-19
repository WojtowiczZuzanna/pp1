numbers = int
numbers = range(1,31)

for number in numbers:
    if number % 3 == 0:
        print("THREE")
    elif number % 5 == 0:
        print("FIVE")
    else: 
        print(number)
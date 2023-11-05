def f(number1, number2, number3):
    numbers = [number1, number2, number3]
    result = max(numbers) - min(numbers)
    return result

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))

print(f(number1, number2, number3))
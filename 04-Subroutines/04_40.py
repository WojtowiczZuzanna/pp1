def f(number):
    result = 0
    for digit in number:
        if number.count(digit) > 1:
            result = result + int(digit)
    return result
number = str(input("Enter a number: "))
print(f(number))
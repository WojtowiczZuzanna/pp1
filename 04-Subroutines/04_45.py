def f(expression):
    result = int(expression[0])
    for i in range(1, len(expression), 2):
        if expression[i] == '+':
            result += int(expression[i+1])
        elif expression[i] == "-":
            result -= int(expression[i+1])
    return result

expression = input("Enter an expression: ")
print(f(expression))
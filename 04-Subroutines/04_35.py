def f(n1, n2, operator):
    if operator == "+":
        return n1 + n2
    elif operator == "%":
        return n1 % n2
    elif operator == "**":
        return n1 ** n2
    elif operator == "*":
        return n1 * n2
    elif operator == "-":
        return n1 - n2
    
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
operator = input("Enter an operator(+, %, **, *, -): ")
print(f"f({n1, n2, operator}) returns {f(n1, n2, operator)}")
def f(amount_to_pay):
    i = 0
    j = 0
    k = 0 
    while amount_to_pay > 0:
        if amount_to_pay // 5:
            i += 1
            amount_to_pay = amount_to_pay - 5

        if 2 <= amount_to_pay < 5:
            amount_to_pay // 2
            j += 1
            amount_to_pay = amount_to_pay - 2
        
        elif amount_to_pay < 2:
            k += 1
            amount_to_pay = amount_to_pay - 1 
    sum = i + j + k
    return sum
amount_to_pay = int(input("Enter the amount: "))
print(f"f({(amount_to_pay)}) minimum coins: {f(amount_to_pay)}")
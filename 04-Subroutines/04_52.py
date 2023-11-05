#basic function
def power(x, n):
    result = x**n
    return result

#function with recursion
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * x ** (n - 1)
    
x = int(input("Enter x: "))
n = int(input("Enter x: "))
print(power(x, n))
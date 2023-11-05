def f(n):
    if n == 1:
        return "*"
    else:
        return "*/" * (n-1) + "*"

n = int(input("Enter n: "))
print(f(n))

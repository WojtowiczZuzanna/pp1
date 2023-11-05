def f(n):
    i = 1
    result = ""
    while i in range(1, n + 1):
        result += str(i)
        i = i + 1
    return result

n = int(input("Enter a number: "))
print(f"f({n}) returns '{f(n)}'")
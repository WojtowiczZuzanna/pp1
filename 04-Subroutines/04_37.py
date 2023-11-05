def f(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        result = [0, 1]
        a = 0
        b = 1
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            result.append(c)
        return result

n = int(input("Enter n: "))
print(f"f({n}) returns {f(n)}")

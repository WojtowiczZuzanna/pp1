def f(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    else:
        return False
    
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))

print(f(n1, n2, n3))
print(f"f({n1, n2, n3}) returns {f(n1, n2, n3)}")

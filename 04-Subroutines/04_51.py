def summ(n):
    add = []
    i = 1
    for i in range(1, n + 1):
        add.append(i)
        i = i + 1
    return sum(add)
    
n = int(input("Enter a number: "))
print(summ(n))

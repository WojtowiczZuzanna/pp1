def f(x,y):
    i = x
    result = []
    while i <= y:
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0:
            result.append(i)
            i = i + 1
        else:
            i = i + 1
            continue
            
    return sum(result)

x = int(input("Enter an x: "))
y = int(input("Enter an y: "))
print(f(x,y))

def f(x, y):
    i = x
    j = 0
    while i in range(x,y):
        if i < 0:
            if i % 2 == 0:
                j = j + 1
                i = i + 1
            else:
                j = j
                i = i + 1
        else:
            break   
    return j

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
print(f(x,y))
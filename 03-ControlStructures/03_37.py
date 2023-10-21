a = "*"

i = 1
j = 2
while 0 < i <=9:
    if 0 < i <= 5:
        print(a * i)
        i = i + 1
    elif 5 < i <= 9:
        print(a * (i - j))
        j = j + 2 
        i = i + 1
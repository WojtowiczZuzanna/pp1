
#i -> numery do 1-49
#j -> 7 liczb w rzędzie 
# -> różnica między sąsiednimi numerami

i = 1 
while i <= 41:
    j = 0
    while j <= 49:
        print(f' {i+j}',end='')
        j = j + 7
        if i + j > 49:
            break
    print()
    i = i + 1
    if i == 8:
        break

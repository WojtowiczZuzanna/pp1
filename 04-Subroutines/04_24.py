import within_range

n = int(input("A number: "))

print(f"number {n} in range <2, 15>: ", end="" )

if within_range.within_range(n, x = 2, y = 16) == True:
    print("yes")
else:
    print("no")
a = int(input("Enter the length of one side of a rectangle: "))
b = int(input("Enter the length of the second side of a rectangle: ")) 

x = "*"
y = " "
i = 1

print(x * a)
for i in range(b - 2):
    print(x,y * (a-4),x)
print(x * a)
i = i + 1

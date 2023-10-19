"""
i = 1
sum = 0
for i in range (1,10):
    while i % 2 == 0:
        sum = sum + 1
        print(sum)
        i = i + 1
"""
sum = 0
i = 1

while i <= 10:
    if i%2 == 0:
        sum = sum + 1
        i = i + 1
print(f"Sum is: {sum}")

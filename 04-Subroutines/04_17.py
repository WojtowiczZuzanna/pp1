n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))


def numbers(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n3 != n1:
        print(f'Numbers{n1}, {n2} and {n3} are different')
        return True
    else:
        return False

print(numbers(n1,n2,n3))


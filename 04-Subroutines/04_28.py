def f(binary_number):
    for char in binary_number:
        if char == "0" or char == "1":
            return True
        else:
            return False
    
binary_number = str(input("Enter a string number: "))
print(f(binary_number))
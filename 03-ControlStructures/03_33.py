decimal_number = int(input("Enter a decimal number: "))

while decimal_number > 0:
    binary_number = ""
    binary_number = str(decimal_number % 2) + binary_number
    decimal_number = decimal_number // 2
    
    print(binary_number)
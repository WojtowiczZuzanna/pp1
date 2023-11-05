def f(product_code):
    if len(product_code) == 4:
        sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
        result = sum % 7

        if int(product_code[3]) == result:
            return True
        else:
            return False
    else:
        return False
       
            

product_code = (input("Enter the code: "))
print(f(product_code))





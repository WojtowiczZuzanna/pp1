number_of_products = int(input("Enter the number of products purchased: "))
price = float(input("Enter product's price: "))

if number_of_products > 2:
    print (f"Amount to pay: {(price * 2) + (number_of_products - 2) * price * 3/4}")
else:
    print (f"Amount to pay: {price * number_of_products}")
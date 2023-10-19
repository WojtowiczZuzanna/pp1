#1
sale = range(0,101)
sale = int(input("What's the sale? (in per cent)"))

if sale >= 10:
    print("Buy the product!! Product price reduced by", sale, "%")

#2
price2 = float(input("Enter current product price: "))
price1 = float(input("Enter previous product price: "))

sale = (1 - price2/price1) * 100

if sale >= 10:
    print("Buy the product!!"
          "Product's price reduced by ", sale,"%")
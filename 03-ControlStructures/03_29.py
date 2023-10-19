



washing_product = input("What do you want to wash? (jacket/underwear/shoes) ")
rinse = input("Do you want additional rinse? (y/n) ")
spin = input("do you want additional spin? (y/n) ")

if rinse == "y":
    rinse = 15
else:
    rinse = 0

if spin == "y":
    spin = 9
else:
    spin = 0

print(f"washing product = {washing_product}")
print(rinse)
print(spin)


if washing_product == "jacket":
    jacket = 40
    print("Total washing time: ", jacket + rinse + spin)

if washing_product == "underwear":
    underwear = 70
    print("Total washing time: ", underwear + rinse + spin)

if washing_product == "shoes":
    shoes = 20
    print("Total washing time: ", shoes + rinse + spin)
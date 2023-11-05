def card_number(number):
    y = ""
    i = 1
    for char in number:
        if i in range(1,17) and char.isdigit():
            if i in range(4,15):
                y += "*"
            else:
                y += char
                i = i + 1
        else:
            y += char
        i = i + 1

    return y 

#number = str(input("Enter card number(16-digits): "))
#print(card_number(number))
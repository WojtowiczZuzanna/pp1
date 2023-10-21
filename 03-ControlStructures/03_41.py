PIN = "0805"

code = (input("Enter PIN code(four-digits): "))
i = 1

if code == PIN:    
    print("Correct")
elif code != PIN:
    while i in range(1,3):
        code = (input("Enter PIN code(four-digits): "))
        i = i + 1
        if code == PIN:    
            print("Correct")
            break
        if i == 3:
            print("The card has been blocked")


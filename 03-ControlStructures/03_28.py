EAN_13 = input("Enter EAN-13 article number: ")

if len(EAN_13) == 13:
    print("Article number is correct")

    if EAN_13 [:3]== "590":
        print("Article manufactured in Poland")


def given_letter():
    phrase = str(input("Enter a phrase: "))
    j = 0
    for char in phrase:    
        if char == "e":
            j = j + 1
            #char = char + 1
    return j
#print (given_letter())
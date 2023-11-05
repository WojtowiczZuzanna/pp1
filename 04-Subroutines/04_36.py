def f(detector):
    plus = []
    minus = []
    i = 0
    j = 0
    for char in detector:
        if char == "+":
            i = i + 1
        elif char == "-":
            j = j + 1
            
    plus.append(i)
    minus.append(j)

    if i >= 3:
        return True
    else:
        return False 


detector = str(input("Enter a string consisting of '+' i '-': "))
print( f"f('{detector}') returns {f(detector)}")
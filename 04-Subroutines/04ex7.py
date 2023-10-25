score = input("Enter the score: ")

def computergrade():
    for score in range(0,1):
        if score < 0.6:
            print("F")
        elif 0.6 <= score < 0.7:
            print("D") 
        elif 0.7 <= score < 0.8:
            print("C")
        elif 0.8 <= score < 0.9:
            print("B")
        elif 0.9 <= score:
            print("A")
        else:
            print("Incorrect format")

print(computergrade())
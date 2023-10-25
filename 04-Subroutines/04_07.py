weight = 81
height = 182

def BMI(weight, height):
    bmi = weight/(height*0.01)**2
    return bmi

print(f"Peter's BMI is {BMI(weight, height)}")
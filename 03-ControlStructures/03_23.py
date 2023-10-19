dog_age = float(input("ENter the dog's age in human years: "))

if 0 < dog_age <= 2:
    dog_age = 10.5
    print(f"The dog's age in dog’s years is {dog_age}")
else:
    dog_age = dog_age * 4
    print (f"The dog's age in dog’s years is {dog_age}")

    
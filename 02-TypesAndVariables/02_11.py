father_income = int(input("Enter father's income: "))
mother_income = int(input("Enter mother's income: "))
people_in_family = int(input("Enter the number of people in the family: "))
sum = father_income + mother_income

print(f"Total income: {sum}")
print(f"Income per person: {sum / people_in_family}")
      
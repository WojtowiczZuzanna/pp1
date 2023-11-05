def f(dice):
    
    max_count = 0 
    current_count = 1
    number = dice[0]
    max_number = number
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_number = dice[i - 1]
            current_count = 1

    if current_count > max_count:
            max_number = dice[-1]
    return max_number 
dice = input("Enter a the number of rolled dice: ")
print(f(dice))
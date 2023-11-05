def f(password):
    if len(password) < 6:
        return False
    
    different = ""
    for char in password:
        if password.count(char) == 1:
            different += char

    
    if len(different) >= 6:
        return True
    else:
        return False

password = str(input("Enter password: "))
print(f(password))
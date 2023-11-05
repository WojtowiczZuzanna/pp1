def f(number,even):

    even_number = []
    odd_number = []

    if even == "True":
        for char in number:
            char = int(char)
            if char % 2 == 0:
                list.append(even_number, char)
        return sum(even_number)
    
    elif even == "False":
        for char in number:
            char = int(char)
            if char % 2 == 1:
                list.append(odd_number, char)
        return sum(odd_number)
    
number = str(input("Enter a number: "))
even = str(input("Enter True/False: "))

print(f(number, even))

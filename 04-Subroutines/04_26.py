f = lambda x: True if x % 2 == 0 else False

x = int(input("A number: "))
if f(x) == True:
    print("A number is even")
else:
    print("A number is odd")
#    if f == 0:
#        return True
#    else:
#        return False

hours = float(input("enter hours: "))
rate = float(input("enter rate:  "))

def computepay(hours, rate):
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * rate * 1.05)
    else:
        pay = hours * rate
    return pay

print(computepay(hours,rate))
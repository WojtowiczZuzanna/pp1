import digits

number = int(input("Enter a number: "))
sum_d = digits.sum_digits(number)           #najpierw podana nazwa modułu "digits." potem nazwa funkcji " .sum_digits"
msg = f"Sum of digits {number} is {sum_d}"
print(msg)

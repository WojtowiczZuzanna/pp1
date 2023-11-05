def is_palindrome(s):
    return s == s[::-1]

s = str(input("Enter a string: "))
print(is_palindrome(s))
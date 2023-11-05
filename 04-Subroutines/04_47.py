def f(text):
    result = ""
    for char in text:
        char += "-"
        result += char
    result = result[:-1]
    return result

text = str(input("Enter a word: "))
print(f(text))

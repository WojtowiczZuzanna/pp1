def f(name):
    word_list = name.split()
    result = ""
    for c in word_list:
        first = c[:1]
        result += first
    return result

name = str(input("Enter a phrase: "))
print(f(name))
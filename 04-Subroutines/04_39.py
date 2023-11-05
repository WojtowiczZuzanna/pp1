def f(sentence):
    new_sentence = ""
    for char in sentence: 
        if char != " ":
            new_sentence = new_sentence + char
    return new_sentence

sentence = str(input("Enter a phrase: "))
print(f(sentence))
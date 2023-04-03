# all upper case letter
# cJJJ 

text = input()

if text.isupper():
    text = text.lower()
elif text.swapcase() == text.capitalize():
    text = text.capitalize()

print(text)
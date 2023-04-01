str1 = input()
str1 = str1.lower()

str2 = ""
str3 = ""
for elem in str1:
    if elem not in "aeiouy":
        str2 += elem

for i in str2:
    str3 = str3 + "." + i 

print(str3)

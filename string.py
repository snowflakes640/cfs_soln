str = str.lower(input())

for i in str:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="y":
        str = str.replace(i, "")
print(str)
for i in str:
    n = str.index(i)
    temp = list(str)
    print(n, i)
    temp.insert(n-1, ".")
    str = "".join(temp)

    
print(str)

word = input()
flag = 1
new = []

while flag == 1:
    for i in word:
        if i == "h":
            new.append(i)
            sub1 = word[word.index(i)+1:]
            flag = 1
            
            break
        else: flag = 0
    if flag == 0: break

    for i in sub1:
        if i == "e":
            new.append(i)
            sub1 = sub1[sub1.index(i)+1:]
            flag = 1
            break
        else: flag = 0
    if flag == 0: break
    
    for i in sub1:
        if i == "l":
            new.append(i)
            sub1 = sub1[sub1.index(i)+1:]
            flag = 1
            break
        else: flag = 0
    if flag == 0: break
    
    for i in sub1:
        if i == "l":
            new.append(i)
            sub1 = sub1[sub1.index(i)+1:]
            flag = 1
            break
        else:
            flag = 0
    if flag == 0: break
    
    for i in sub1 :
        if i == "o":
            new.append(i)
            sub1 = sub1[sub1.index(i)+1:]
            flag = 1
            break
        else: flag = 0
    if flag == 0: break

    break

if flag == 1 and len(new)==5: print("YES")
else: print("NO")
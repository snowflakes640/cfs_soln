number = input()
ind = None
for bit in number:
    if bit == "0":
        ind = number.index(bit)
        break
num = []
if ind == None:
    num = number[:-1]
else:
    for i in range(len(number)):
        #print(bit, number.index(bit))
        if i == ind:
            #print(bit, number.index(bit), ind)
            pass
        else: num.append(number[i])
combined_num = int("".join(num))
print(combined_num)
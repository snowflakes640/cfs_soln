num = input()

ref = 0
i = 0
cnt = 0

while True:
    if i>= len(num) or ref>= len(num): break
    if num[ref] == num[i]:
        #print(f"ref {num[ref]} i {num[i]}")
        i+=1
        cnt+=1
    else:
        #print(f"ref {num[ref]} i {num[i]}")
        ref = i
        cnt = 0 
    if cnt == 7:
        print("YES") 
        break
#print(cnt)
if cnt != 7: print("NO")


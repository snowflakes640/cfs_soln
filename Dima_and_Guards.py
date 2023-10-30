max = int(input())
guards = [list(map(int, input().split())) for i in range(4)]
#print(guards)
flag = 0

for row in range(4):
    for col1 in range(2):
        if guards[row][col1] + guards[row][2] <= max:
            guardBox = row+1
            gift1 = guards[row][col1]
            gift2 = max - gift1
            flag = 1
            break
        
        elif guards[row][col1] + guards[row][3] <= max:
            guardBox = row+1
            gift1 = guards[row][col1]
            gift2 = max - gift1
            flag = 1
            break
    if flag == 1: break

if flag == 1: print(guardBox, gift1, gift2)
else: print(-1)




matrix = []
for i in range(4):
    matrix.append(list(input()))

flag = False
for row in range(3):
    for col in range(3):
        mark = 1
        x = matrix[row][col]
        if matrix[row][col+1] == x: mark=mark +1
        if matrix[row+1][col] == x: mark=mark +1
        if matrix[row+1][col+1] == x: mark=mark +1

        if row == 2 and col ==2 and mark == 1:
            flag = True
            print("YES") 

        if mark==3 or mark==4 :
            flag = True
            print("YES")
            break
    if flag == True:break

if flag == False: print("NO")


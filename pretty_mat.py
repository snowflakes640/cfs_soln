matrix = []
r = 5
c = 5
for i in range(r):
    rows = list(map(int, input().split()))
    matrix.append(rows)

for i in range(r):
    for j in range(c):
        if matrix[i][j]==1:
            break
    if matrix[i][j] == 1:
        break
      
p = i - 2
q = j - 2
print((abs(p)+abs(q)))
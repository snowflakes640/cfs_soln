n = int(input())
cnt = 0

arr = []
for i in range(n):
         row = list(map(int, input().split()))
         arr.append(row)


for i in range(n):
    s = 0
    for j in range(3):
        s += arr[i][j]
    if s>=2:
        cnt += 1

print(cnt)
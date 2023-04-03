n = int(input())
vectors = []
for i in range(n):
    scores = []
    scores = list(map(int, input().split()))
    vectors.append(scores)
x, y, z = 0, 0, 0

for i in vectors:
    x += i[0]
    y += i[1]
    z += i[2]

if x==0 and y==0 and z==0:
    print("YES")
else: print("NO")

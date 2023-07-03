import math
n, k = map(int, input().split())
l = math.ceil(n/2)
if k <= l:
    print(2*k -1)
else: print(2*(k-l))














# fin = []
# pos = 0
# pose = int(n/2) 
# for i in range(1,n+1):
#     if i%2 != 0:
#         fin.insert(pos, i)
#         pos += 1
#     else:
#         fin.insert(pose, i)
#         pose += 1


# print(fin[k-1])
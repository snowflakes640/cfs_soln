nums = list(map(int, input().split()))
sum = 0

for i in nums:
    sum += i

if sum%5==0 and sum!=0:
    print(int(sum/5))
else: print(-1)
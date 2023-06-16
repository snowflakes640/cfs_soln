import math
m, n , a = (map(int, input().split()))

rem_r = math.ceil(m/a)
#print(rem_r)

rem_c = math.ceil(n/a)
#print(rem_c)

result = rem_c*rem_r

print(result)

n = int(input())
line = list(map(int, input().split()))
#print(line)

sum25 = 0
sum50 = 0
sum100 = 0
flag = 0
def ret(ruble):
    return ruble - 25

for i in range(n):
    if line[i]==25:
        sum25 += 25
    elif line[i]==50:
        sum50 += 50
        if sum25==0:
            print("NO")
            flag = 1
            break
        else: sum25 -= 25
    elif line[i]==100:
        sum100 += 100
        if sum25 == 0:
            print("NO")
            flag = 1
            break
        elif sum50 != 0:
            sum50 -= 50
            sum25 -= 25
        elif sum25 >= 75:
            sum25 -= 75
        else:
            print("NO")
            flag = 1
            break

if flag == 0: print("YES")









# for i in range(n):
#     if ret(line[i]) > cash:
#         flag = 0
#         print("NO")
#         break
#     else:
#         cash = cash - ret(line[i]) + line[i]
#         flag = 1
    
# if flag == 1: print("YES")
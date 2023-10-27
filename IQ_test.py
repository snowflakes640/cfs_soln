n = int(input())
flag = 0
numbers = list(map(int, input().split()))
#print(numbers)

for i in range(3):
    if numbers[i]%2 == 0: flag = flag + 2
    else: flag = flag + 1

if flag == 7 or flag == 6 or flag ==5: type = 0
else: type = 1 
#print(type)
if type == 0:
     for i in numbers:
          if i%2 != 0:
               ind = numbers.index(i)
               break
else:
     for i in numbers:
          if i%2 == 0:
               ind = numbers.index(i)
               break
          
print(ind+1)

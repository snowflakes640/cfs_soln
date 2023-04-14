from math import sqrt

def isPrime(n):
    if (n <= 1):
        return False
 
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True

x , y = map(int, input().split())
prime = []


for i in range(x, y+1):
    if isPrime(i):
        prime.append(i)
        #print(prime)
        if len(prime) > 2:
            break


if len(prime)>1:
    if isPrime(y) and prime[1] == y:
        print("YES")
    else: print("NO")
else: print("NO")

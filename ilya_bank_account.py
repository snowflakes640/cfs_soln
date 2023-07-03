balance = int(input())

if balance < 0:
    balance = abs(balance)
    listed = list(map(int, str(balance)))
    try1 = listed[:len(listed)-1]
    del listed[-2]


    def convert(list):
        s = [str(i) for i in list]
        b2int = int("".join(s))     
        return(b2int)

    if convert(try1) <= convert(listed): print(-abs(convert(try1)))
    else: print(-abs(convert(listed)))
else: print(balance)
n = int(input())
if 1<=n<=100:
    wrdlist = []
    for i in range(0,n):
        wrdlist.append(input())

    all= " ".join(wrdlist)

    for wrd in all.split():
        x = len(wrd)
        if x>10:
            print(wrd[0]+ str(x-2) + wrd[x-1])
        else:
            print(wrd)
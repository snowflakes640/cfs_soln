x, y = map(int, input().split())
new_scr = []
if x <= 50 and x>=1 and y<=x:
    scores = list(map(int, input().split()))
        
    for i in range(x):
        if scores[i]>=scores[y-1]:
            if scores[i] > 0:
                new_scr.append(scores[i])
        
    print(len(new_scr))



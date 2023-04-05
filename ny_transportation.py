#taking inputs
n, t = map(int,input().split())
a_values = list(map(int,input().split()))

#creating traverse list
graph = {}
for cell in range(1, n):
    graph[cell] = [cell+ a_values[cell-1]]
#print(graph)

#creating list to check (same as dfs)
explore = []
explore.append(1)
mark = set()
flag = 1

while len(explore)>0:
    current = explore.pop(0)
    if current not in mark and current in graph.keys():
        mark.add(current)
        for j in graph[current]:
            if j!=t:
                explore.append(j)
            else:
                flag = 0
                print("YES")
                break
if flag != 0:
    print("NO")
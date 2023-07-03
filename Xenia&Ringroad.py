n , m = map(int, input().split())
task_room = list(map(int, input().split()))
l = len(task_room) -1

#i = task_room[0]
time = task_room[0]-1
for i in range(l):
    next = i + 1
    if task_room[next] < task_room[i]:
        #print(f"smol {task_room[i], task_room[next]}")
        time += n - task_room[i] + task_room[next]
        #print(time)
    elif task_room[next] == task_room[i]:
        #print(f"eq {task_room[i], task_room[next], time}")
        pass
    elif task_room[next] > task_room[i]:
        #print(f"big {task_room[i], task_room[next]}")
        time += task_room[next] - task_room[i]
        #print(time)
print(time)

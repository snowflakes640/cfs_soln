data = ([2, 3])
sorted(data, key:)

































# strn , n = map(int,input().split())
# data = []
# sorted_data = []
# flag = 0
# for i in range(n):
#     data.append(list(map(int, input().split())))

# def sort(data_list, x):
#     for i in data_list:
#         if i[0] < x:
#             sorted_data.append(i)

# def not_empty(l):
#     if len(l) != 0: return True
#     else: return False

# sort(data, strn)
# #print(data, sorted_data)

# it = 1
# while it < n:
#     if not_empty(sorted_data):
#         #print(sorted_data[0])
#         tup = sorted_data[0]
#         if tup[0] < strn:
#             strn += tup[1]
#             data.remove(tup)
#             sorted_data.remove(tup)
#             sort(data,strn)
#             flag = 1
#         else: flag = 0
#     else: break
    

# if flag == 1: print("YES")
# else: print("NO")

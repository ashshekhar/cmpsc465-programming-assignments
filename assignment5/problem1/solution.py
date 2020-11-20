def binary_search(interval_list, k, a, b):
  m = (a+b)//2

  if((interval_list[m][1] <= interval_list[k][0]) and (interval_list[k][0] <= interval_list[m+1][1])):
    return m
    print("return m")
  
  elif(interval_list[m][1] > interval_list[k][0]):
    return binary_search(interval_list, k, a, m)
    print("return 1")

  elif(interval_list[k][0] > interval_list[m+1][1]):
    return binary_search(interval_list,k, m+1, b)
    print("return 2")

  else:
    return 0

def weighted_interval_scheduling(interval_list):

  for k in range(1, num_jobs):
    print("Hello")
    pre[k] = binary_search(interval_list, k, 1, k-1)
    print("Hi")
    F[k] = max(F[k-1], F[pre[k]]+interval_list[k][2])

  return F[num_jobs]

num_jobs = int(input())
interval_list = []

for edge in range(num_jobs):
  interval_input = input()
  intervals = list(map(int, interval_input.strip().split(' ')))
  interval_list.append(intervals)

interval_list.sort(key=lambda x:x[1])

F = [0]*(num_jobs+1)
pre = [0]*(num_jobs+1)

print(weighted_interval_scheduling(interval_list))


  


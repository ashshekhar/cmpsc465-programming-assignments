def binary_search(interval_list, k, a, b):
  m = (a+b)//2

  if(a == b):
    return a

  if((interval_list[m][1] <= interval_list[k][0]) and (interval_list[k][0] <= interval_list[m+1][1])):
    return m
  
  elif(interval_list[m][1] > interval_list[k][0]):
    return binary_search(interval_list, k, a, m)

  elif(interval_list[k][0] > interval_list[m+1][1]):
    return binary_search(interval_list, k, m+1, b)

  else:
    return 0

def weighted_interval_scheduling(interval_list):

  for k in range(1, num_jobs):
    pre[k] = binary_search(interval_list, k, 0, k-1)
    F[k] = max(F[k-1], F[pre[k]]+interval_list[k][2])

  return F[num_jobs-1]

num_jobs = int(input())
interval_list = []

for edge in range(num_jobs):
  interval_input = input()
  intervals = list(map(int, interval_input.strip().split(' ')))
  interval_list.append(intervals)

interval_list.sort(key=lambda x:x[1])
print(f"Sorted list by end time: {interval_list}")

F = [0]*(num_jobs)
pre = [0]*(num_jobs)

print(weighted_interval_scheduling(interval_list))


  


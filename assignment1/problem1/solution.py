array_list_1 = input()
array_list_2 = input()

array_list_1 = array_list_1.split(" ")
array_list_2 = array_list_2.split(" ")

num_1 = int(array_list_1[0])
num_2 = int(array_list_2[0])

array_list_1 = list(map(int, array_list_1[1:]))
array_list_2 = list(map(int, array_list_2[1:]))

merge_sorted_array = []
pointer_1 = 0 
pointer_2 = 0

while pointer_1<num_1 and pointer_2<num_2:
  if(array_list_1[pointer_1] < array_list_2[pointer_2]):
    merge_sorted_array.append(array_list_1[pointer_1])
    pointer_1 += 1

  else:
    merge_sorted_array.append(array_list_2[pointer_2])
    pointer_2 += 1
  
if pointer_1>=num_1:
  merge_sorted_array.extend(array_list_2[pointer_2:num_2])

if pointer_2>=num_2:
  merge_sorted_array.extend(array_list_1[pointer_1:num_1])

merge_sorted_array.insert(0, num_1+num_2)
print(*merge_sorted_array, sep=' ')

def merge_sort(array_list):

  array_length = len(array_list)

  if array_length<=1:
    return array_list
  
  half_length = int(array_length/2)

  array_half_1 = merge_sort(array_list[:half_length])
  array_half_2 = merge_sort(array_list[half_length:])

  return merge_two_sorted_arrays(array_half_1, array_half_2)

def merge_two_sorted_arrays(array_list_1, array_list_2):

  num_1 = len(array_list_1)
  num_2 = len(array_list_2)
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

  return merge_sorted_array

def main():

  array_length = input()
  array_list = input()

  array_list =  array_list.split(" ")
  array_list = list(map(int, array_list))

  print(*merge_sort(array_list), sep=" ")

main()
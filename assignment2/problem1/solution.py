def merge_two_sorted_arrays_and_count(array_list_1, array_list_2):
  
  num_1 = len(array_list_1)
  num_2 = len(array_list_2)
  merge_sorted_array = []

  pointer_1 = 0 
  pointer_2 = 0
  inversion_count = 0

  while pointer_1<num_1 and pointer_2<num_2:
    if(array_list_1[pointer_1] < array_list_2[pointer_2]):
      merge_sorted_array.append(array_list_1[pointer_1])
      pointer_1 += 1

    else:
      merge_sorted_array.append(array_list_2[pointer_2])
      inversion_count = inversion_count + ((num_1 - pointer_1))
      pointer_2 += 1
    
  if pointer_1>=num_1:
    merge_sorted_array.extend(array_list_2[pointer_2:num_2])

  if pointer_2>=num_2:
    merge_sorted_array.extend(array_list_1[pointer_1:num_1])
  
  return inversion_count, merge_sorted_array


def recursive_count(input_array):

  inversion_count = 0
  
  array_length = len(input_array)

  if array_length<=1:
    return 0, input_array
    
  half_length = int(array_length/2)
  array_half_1 = input_array[:half_length]
  array_half_2 = input_array[half_length:]

  count_1, array_half_1 = recursive_count(array_half_1)
  count_2, array_half_2 = recursive_count(array_half_2)
  count_3, input_array = merge_two_sorted_arrays_and_count(array_half_1, array_half_2)

  inversion_count += count_1 + count_2 + count_3

  return inversion_count, input_array

def main():

  line_1 = input()
  line_2 = input()

  line_1 = line_1.strip().split(' ')
  line_2 = line_2.strip().split(' ')

  array_1 = []
  array_2 = []

  array_1 = list(map(int, line_1[:]))
  array_2 = list(map(int, line_2[:]))

  print(recursive_count(array_2)[0])

main()
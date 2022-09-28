from typing import List

def insertionSort(array) -> List[int]:
  for i in range(len(array)):
    element = array[i]
    j = i-1
    while j >= 0 and array[j] > element:
      array[j+1] = array[j]
      j -= 1
    array[j+1] = element
  return array

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))

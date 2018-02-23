
#len(arr1) = n
#len(arr2) = m
# RUNTIME = O(n + m)
# SPACE = O(n + m)

# arr1 is sorted
# arr2 is sorted

#input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]
# i = 0, j =0
# i means arr1 index
# j means arr2 index

# while
#   if arr1[i] == arr[j]
#      duplicates.append(arr1[i])
#      i += 1
#      j += 1
#   else if
#      i += 1
#   else
#      j += 1

# SPACE O(N) if N < M or O(M) if M < N
# TIME O(N) if N < M or O(M) if M < N

# M = N^2
# M is big

# your code
# TIME O (N + M) = O (N + N^2) = 0(N^2)

# using binary search
# TIME O (N + logM) = O(N + log N^2)

def find_duplicates(arr1, arr2):
  duplicates = []
  i, j = 0, 0
  end_reached = False

  while end_reached == False:
    if arr1[i] == arr2[j]:
      duplicates.append(arr1[i])
      i += 1
      j += 1
    elif arr1[i] > arr2[j]:
      j += 1
    else:
      i += 1
    if i >= len(arr1) or j >= len(arr2):
      return duplicates

'''
def find_duplicates(arr1, arr2):
  pass # your code goes here
  set_a = set(arr1)
  set_b = set(arr2)
  intersection_a_b = set_a.intersection(set_b)
  return sorted(list(intersection_a_b))
'''

# O(N⋅log(M))

https://www.facebook.com/yusuke.itabashi.9

function findDuplicates(arr1, arr2):
    duplicates = []

    for number in arr1:
        if binarySearch(arr2, number) != -1:
            duplicates.push(number);

    return duplicates


function binarySearch(arr, num):
    begin = 0
    end = arr.length - 1

    while (begin <= end):
        mid = begin + floor((end-begin)/2)
        if arr[mid] < num:
            begin = mid + 1
        else if arr[mid] == num:
            return mid
        else:
            end = mid - 1

    return -1

print find_duplicates([1, 2, 3, 5, 6, 7],[3, 6, 7, 8, 20])

 #https://www.facebook.com/coreyharrilal123

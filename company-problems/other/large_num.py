# Given an integer array, find the top k largest numbers in it.




def find_min(array): # return min
    min_num = array[0]
    for num in array:
        if num < min_num:
            min_num = num
    return min_num


def k_largest(arr, k):
    top_k = arr[0:k] # first k elements
    print 'first k elements',top_k
    min_num = find_min(top_k)
    print 'min is: ',min_num
    arr = arr[k:]
    for index, num in enumerate(arr):
        if num > min_num:
            print 'num is greater than min. num is: ',num,' min is: ',min_num
            top_k.remove(min_num)
            top_k.append(num)
            min_num = find_min(top_k)
            print 'new min is: ',min_num
        print 'top_k is: ',top_k
    return top_k

print k_largest([8,4,3,10,6], 3)
print k_largest([1, 6, -100, 40, 3], 3)
print k_largest([3,10,1000,-99,4,100], 3)

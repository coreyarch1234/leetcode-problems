cycle_length_arr = []

def cycle_length(num_one):
    cycle_length_one = 1
    while num_one != 1:
        if num_one % 2 == 0:
            num_one = num_one / 2
        else:
            num_one = 3*num_one + 1
        cycle_length_one += 1
        print num_one
        print 'cycle_length_one',cycle_length_one
    return cycle_length_one

def all_cycle_lengths(start, end):
    for num in range(start, end + 1):
        cycle_length_arr.append(cycle_length(num))
    print 'num is: ',cycle_length_arr
    return max(cycle_length_arr)


# print cycle_length(10)
print all_cycle_lengths(1, 10)

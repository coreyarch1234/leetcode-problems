# https://www.getpy.com/hashtable/challenge?picky-eater
#
#
# Picky Eater
# There are k restaurants in town. You eat at one of them each day and each serves a different meal every day. You need to find the most enjoyment you can get over n days eating at these restaurants. You cannot eat at the same restaurant two days in a row.
#
# The restaurant meals are a n by k array of arrays of numbers, where meals[i][j] represents the enjoyment you get on day i eating at restaurant j.
#
# Example input:
#
# [[1, 2, 3],
#  [5, 1, 2],
#  [9, 8, 6]]
# Output:
#
# 16
# Explanation:
#
# One day 0, you eat a restaurant 2. Enjoyment: 3
# One day 1, you eat a restaurant 0. Enjoyment: 5
# One day 2, you eat a restaurant 1. Enjoyment: 8
# Total enjoyment: 16
# You cannot eat at restaurant 0 on day 2 because it is better to eat at restaurant 0 on day 1 to get the 5 enjoyment.

# DIDN'T SOLVE. COME BACK TO LATER


def right_restaurant_max(restaurant_one, restaurant_two):
    # restaurant_one_max = max(restaurant_one)
    # restaurant_one.remove(restaurant_one_max)
    # restaurant_one_second_max = max(restaurant_one)
    #
    # restaurant_two_max = max(restaurant_two)
    # restaurant_two.remove(restaurant_two_max)
    # restaurant_two_second_max = max(restaurant_two)

    restaurant_one_copy = restaurant_one[:]
    restaurant_two_copy = restaurant_two[:]
    print "restaurant_one: ",restaurant_one
    print "restaurant_two: ",restaurant_two
    print
    restaurant_one_max = max(restaurant_one_copy)
    restaurant_one_copy.remove(restaurant_one_max)
    restaurant_one_second_max = max(restaurant_one_copy)

    restaurant_two_max = max(restaurant_two_copy)
    restaurant_two_copy.remove(restaurant_two_max)
    restaurant_two_second_max = max(restaurant_two_copy)

    if restaurant_one_max + restaurant_two_second_max >= restaurant_one_second_max + restaurant_two_max:
        return [restaurant_one_max, restaurant_two_second_max]
    else:
        return [restaurant_one_second_max, restaurant_two_max]



def solution(restaurants):
    # Type your solution here
    curr_arr = restaurants[0] # [1, 2, 3]
    next_arr = restaurants[1]

    curr_pair = [] # [max, index]
    next_pair = []

    max_enjoyment = 0

    for index, row in enumerate(restaurants):
        if index < len(restaurants) - 1:
            next_restaurant = restaurants[index + 1]
            curr_max = max(row)
            next_max = max(next_restaurant)
            curr_pair, next_pair = [curr_max, row.index(curr_max)], [next_max, next_restaurant.index(next_max)]

            if curr_pair[1] != next_pair[1]:
                max_enjoyment += curr_pair[0]
            else:
                max_enjoyment += right_restaurant_max(row, next_restaurant)[0]
                # max_enjoyment += 5
            prev_restaurant = row
        else:
            print "calling else: ",prev_restaurant
            print "and",row
            print "max_stuff",right_restaurant_max(row, next_restaurant)[0]
            max_enjoyment += right_restaurant_max(prev_restaurant, row)[1]
    return max_enjoyment




print solution([[1, 2, 3],
 [5, 1, 2],
 [9, 8, 6]])

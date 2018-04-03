# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
#
#
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
#
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
#
# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).


def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    restaurant_dict = {}
    min_sum = None
    min_restaurant = []
    for index, name in enumerate(list1):
        restaurant_dict[name] = index
    print restaurant_dict
    for index, name in enumerate(list2):
        if name in restaurant_dict:
            if min_sum == None:
                min_sum = index + restaurant_dict[name]
                min_restaurant = [name]
            else:
                if index + restaurant_dict[name] == min_sum:
                    min_restaurant.append(name)

                if index + restaurant_dict[name] < min_sum:
                    min_sum = index + restaurant_dict[name]
                    min_restaurant = [name]
    return min_restaurant

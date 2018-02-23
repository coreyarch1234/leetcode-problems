# https://leetcode.com/problems/two-sum/description/


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    solution_set = set()
    for index, number in enumerate(nums):
        if (target - number) in nums[index + 1:] or (target - number) in nums[:index]:
            print target - number
            solution_set.add(index)
    return list(solution_set)

# print twoSum([3,3], 6)


def twoSumImproved(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # make dict
    target_map = {}
    for index, num in enumerate(nums):
        if num not in target_map:
            target_map[num] = [index]
        else:
            target_map[num] += [index]


    solution_list = []
    print target_map
    for index, num in enumerate(nums):
        compliment = target - num
        if (compliment in target_map.keys() and index != target_map[compliment][0]):
            if len(target_map[compliment]) == 2:
                return target_map[compliment]
            else:
                print compliment
                print target_map[compliment]
                target_map[compliment] += [index]
                return target_map[compliment]
    return solution_list


# print twoSumImproved([3,3], 6)

def twoSumImprovedMore(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # make dict
    target_map = {}
    for index, num in enumerate(nums):
        compliment = target - num
        if compliment in target_map.keys():
            return [index, target_map[compliment]]
        else:
            target_map[num] = index



print twoSumImprovedMore([2, 7, 11, 15], 9)

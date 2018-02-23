
import random
def pick(target, nums):
    """
    :type target: int
    :rtype: int
    """
    len_nums = len(nums)
    found = False
    while found == False:
        random_indices = []
        for num in nums:
            random_indices.append(random.randint(0, len_nums - 1))
        for index in random_indices:
            if nums[index] == target:
                found = True
                return index

print pick(3, [1,2,3,3,3])

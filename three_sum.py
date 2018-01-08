# 3Sum
# https://leetcode.com/problems/3sum/description/

def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sum_dict = {}
        for index_number, number in enumerate(nums):
            compliment_sum = -1 * number
            target_map = {}
            for index, num in enumerate(nums):
                compliment = compliment_sum - num
                if index != index_number:
                    if compliment in target_map.keys():
                        key = 1
                        second_num = nums[index]
                        third_num = nums[target_map[compliment]]
                        key *= abs(number) if number != 0 else 1
                        key *= abs(second_num) if second_num != 0 else 1
                        key *= abs(third_num) if third_num != 0 else 1
                        sum_dict[key] = [number, second_num, third_num]
                    else:
                        target_map[num] = index
        return sum_dict.values()

print threeSum([-1, 0, 1, 2, -1, -4])

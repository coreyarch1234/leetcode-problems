# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
#
# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    digit_letter_dict = {"2": "abc",
                         "3": "def",
                         "4": "ghi",
                         "5": "jkl",
                         "6": "mno",
                         "7": "pqrs",
                         "8": "tuv",
                         "9": "wxyz"}
    if len(digits) == 1:
        return list(digit_letter_dict[digits])
    if len(digits) == 0:
        return []
    digit_length = len(digits)
    queue = list(digit_letter_dict[digits[0]])
    index = 1
    current_arr = digit_letter_dict[digits[index]]
    done = False

    while done == False:
        next_queue = []
        for letter in queue:
            for char in current_arr:
                next_queue.append(letter + char)
        queue = next_queue
        index += 1

        if index > digit_length - 1:
            done = True
        else:
            current_arr = digit_letter_dict[digits[index]]
    return queue



print letterCombinations("23456")

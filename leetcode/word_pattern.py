# https://leetcode.com/problems/word-pattern/description/
#
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
#
# Mock interview problem - leetcode - correct
# time elapsed: 22 min and 5 sec out of 25 min
#
#


def wordPattern(self, pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    str_list = str.split(' ')
    pattern_dict = {}
    reverse_dict = {}
    # print str_list

    # check if same word
    if pattern == str:
        return False

    # check if not same length
    if len(pattern) != len(str_list):
        return False

    for index, word in enumerate(str_list):
        if word in reverse_dict:
            if reverse_dict[word] != pattern[index]:
                return False
        else:
            reverse_dict[word] = pattern[index]

    for index, letter in enumerate(pattern):
        if letter in pattern_dict:
            # print pattern_dict
            # print "letter repeat:",letter
            # print "pattern_dict[letter]: ",pattern_dict[letter]
            # print "str_list[index]: ",str_list[index]
            if pattern_dict[letter] == str_list[index]:
                continue
            else:
                return False
        else:
            pattern_dict[letter] = str_list[index]
    return True

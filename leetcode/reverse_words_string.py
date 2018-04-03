# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    if len(list(set(s))) == 1 and list(set(s)) == ' ':
        print ' case in point'
        return ''
    s_list = s.split(' ')
    return ' '.join(s_list[::-1])

# print reverseWords("the sky is blue")
print reverseWords(" ")

# https://leetcode.com/problems/longest-common-prefix/description/
# Write a function to find the longest common prefix string amongst an array of strings.

#get common prefix between 2 strings
def commonPrefix(str1, str2):
    common_prefix = ""
    if len(str1) <= len(str2):
        for index, char in enumerate(str1):
            if char == str2[index]:
                common_prefix += char
            else:
                return common_prefix
        return common_prefix
    else:
        for index, char in enumerate(str2):
            if char == str1[index]:
                common_prefix += char
            else:
                return common_prefix
        return common_prefix

# print commonPrefix("apple", "app")


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    print "reached start and strs is: " + str(strs)
    if len(strs) == 1:
        return strs[0]
    if len(strs) == 2:
        print "the common strings are: " + strs[0] + " and " + strs[1]
        return commonPrefix(strs[0], strs[1])
    if len(strs) > 2:
        midpoint = len(strs) // 2
        left_prefix = longestCommonPrefix(strs[:midpoint])
        right_prefix = longestCommonPrefix(strs[midpoint:])
        print "left prefix is: " + left_prefix
        print "right prefix is: " + right_prefix
        return commonPrefix(left_prefix, right_prefix)


print longestCommonPrefix(["c","acc","ccc"])
# print longestCommonPrefix(["leets", "leetcode", "leeter", "leetcoder", "leet", "leety", "leey", "lee", "leetify", "leetch"])

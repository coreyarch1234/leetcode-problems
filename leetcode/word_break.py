# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
#
# https://leetcode.com/problems/word-break/description/

break_memo = []
def wordBreak(s, wordDict, start = 0, end = 1):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if end >= len(s):
            if s[start:end] in wordDict:
                print 'word final in wordDict: ' + s[start:end]
                return True
            else:
                print 'word final not in wordDict: ' + s[start:end]
                return False
        if s[start:end] in wordDict: # if found
            print 'word in wordDict: ' + s[start:end]
            print 'start and end: ' + str(start) + ': ' + str(end)
            print
            return wordBreak(s, wordDict, end, end + 1)
        else:
            print 'word not in wordDict: ' + s[start:end]
            print 'start and end: ' + str(start) + ': ' + str(end)
            print
            return wordBreak(s, wordDict, start, end + 1)


print wordBreak("leetcodeappled", ["leet", "code", "apple"])

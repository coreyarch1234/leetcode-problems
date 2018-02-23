# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# https://leetcode.com/problems/group-anagrams/description/

def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group_anagrams = {}
        for word in strs:
            if tuple(sorted(word)) not in group_anagrams:
                group_anagrams[tuple(sorted(word))] = [word]
            else:
                group_anagrams[tuple(sorted(word))].append(word)
        return group_anagrams.values()


print groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

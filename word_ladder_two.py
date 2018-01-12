# https://leetcode.com/problems/word-ladder-ii/description/
#
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.


# GO OVER WITH ALAN
def findLadders(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    index_status = {}
    index_status_copy = {}
    for index,letter in enumerate(beginWord):
        if letter == endWord[index]:
            index_status[index] = True
            index_status_copy[index] = True
        else:
            index_status[index] = False
            index_status_copy[index] = False

    letters_ordered = {}
    index = 0
    while index <= len(beginWord) - 1:
        letter_list = set()
        for word in wordList:
            letter_list.add(word[index])
        letters_ordered[index] = letter_list
        index += 1
    print letters_ordered

    transformation_list = []
    transformation_bank = {}

# print findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])


for letter in set(['h', 'a', 't']):
    print letter

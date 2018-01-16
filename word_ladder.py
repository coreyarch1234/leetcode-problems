# https://leetcode.com/problems/word-ladder/description/
#
#
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    index_status = {} # index and if that letter is correct in endWord
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
    current_word = beginWord
    index = 0
    while current_word != endWord:
        print "index: ", index
        if index == len(beginWord):
            index = 0
        for letter in letters_ordered[index]:
            temp_word = current_word[:index] + letter + current_word[index + 1:]
            if temp_word == current_word:
                continue
            print "temp word: " + temp_word
            if temp_word in wordList:
                transformation_list.append(temp_word)
                print "appended: ", transformation_list
                current_word = temp_word
                if temp_word == endWord:
                    print "done"
                    return transformation_list

        index += 1

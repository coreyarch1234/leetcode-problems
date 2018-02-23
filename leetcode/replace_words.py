# In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.
#
# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.
#
# You need to output the sentence after the replacement.
#
# Example 1:
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

#right answer

# Intuition
#
# For each word in the sentence, we'll look at successive prefixes and see if we saw them before.
#
# Algorithm
#
# Store all the roots in a Set structure. Then for each word, look at successive prefixes of that word. If you find a prefix that is a root, replace the word with that prefix. Otherwise, the prefix will just be the word itself, and we should add that to the final sentence answer.

def replaceWords(self, roots, sentence):
    rootset = set(roots)

    def replace(word):
        for i in xrange(1, len(word)):
            if word[:i] in rootset:
                return word[:i]
        return word

    return " ".join(map(replace, sentence.split()))


# attempted solution - wrong
# class Solution(object):
#     def replaceWords(self, dict, sentence):
#         """
#         :type dict: List[str]
#         :type sentence: str
#         :rtype: str
#         """
#         sentence = sentence.split(' ')
#         temp_sentence = sentence[:]
#         sentence = sorted(sentence)
#         dict_list = sorted([[word, len(word), 'off'] for word in dict])
#         # print 'dict_list ',dict_list
#         sentence_len = len(sentence)
#         dict_len = len(dict_list)
#         sen_i = 0
#         dict_i = 0
#         # point_sen = sentence[sen_i]
#         # point_dict = dict_list[dict_i]
#         end_reached = False
#         # print point_dict[0]
#         # print point_sen[:point_dict[1]]
#         # print point_dict
#         while end_reached == False:
#             if sen_i >= sentence_len or dict_i >= dict_len:
#                 return ' '.join(temp_sentence)
#             point_sen = sentence[sen_i]
#             point_dict = dict_list[dict_i]
#             print 'point_sen: ',point_sen
#             print 'point_dict: ',dict_list[dict_i]
#             if point_dict[0] == point_sen[:point_dict[1]]:
#                 print 'they are equal: ',
#                 point_dict[2] = 'on'
#                 temp_sentence = [word.replace(point_sen,point_dict[0]) for word in temp_sentence]
#                 print 'temp_sentence is now: ',temp_sentence
#                 sen_i += 1
#             else:
#                 if point_dict[2] == 'on':
#                     dict_i += 1
#                 else:
#                     sen_i += 1

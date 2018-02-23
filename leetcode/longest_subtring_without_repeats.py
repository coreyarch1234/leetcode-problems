# # Complete the function below.
#
# def findNonRepeatSubstring(str): #return length of non repeating substring
#     repeat_dict = {}
#     for index, letter in enumerate(str):
#         if letter in repeat_dict:
#             return index
#         repeat_dict[letter] = True
#     return len(str)
#
# def longestSubstring(str):
#     if len(set(str)) == 1:
#         return str[0]
#     index = 0
#     curr_max_len = 1
#     curr_max_pair = (index, curr_max_len) #(index, length)
#     str_len =  len(str)
#     while index <= str_len:
#         string = str[index:]
#         curr_len = findNonRepeatSubstring(string)
#         if curr_len > curr_max_len:
#             curr_max_pair = (index, curr_len)
#             curr_max_len = curr_len
#         index += 1
#     print 'curr_max_pair',curr_max_pair
#     return ''.join(set(str[curr_max_pair[0]:curr_max_pair[1] + 1]))


def longestSubstring(str):
    start = 0
    end = 0
    repeat_dict = {}
    len_str = len(str)
    max_str = ""
    curr_str = ""
    str_list = []
    while end <= len_str - 1:
        print "start, end",start,end
        print "repeat_dict", repeat_dict
        if str[end] not in repeat_dict:
            repeat_dict[str[end]] = True
            curr_str += str[end]
            end += 1
            print "not in** word is now: ",curr_str
        else:
            if len(curr_str) > len(max_str):
                max_str = curr_str
            repeat_dict = {}
            repeat_dict[str[end]] = True
            start = end
            end += 1
            curr_str = ""
            print "there is a repeat"
    return max_str



s = "aaaa"
s1 = "abcdaef"
s2 = "abcabcdefa"
print longestSubstring(s1)

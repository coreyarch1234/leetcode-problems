# https://www.interviewcake.com/question/python/find-rotation-point
#
# I want to learn some big words so people think I'm smart.
#
# I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know. I put each word I didn't know at increasing indices in a huge list I created in memory. When I reached the end of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.
#
# Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered list that has been "rotated." For example:
#
#   words = [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',  # <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]
#
# Write a function for finding the index of the "rotation point," which is where I started working from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so we want to be efficient here.


#
# def word_rotation(word_array): # O(N)
#     # create way to check if words are in alphabetical order
#     # recursively call this and return False when word is out of order and return the index
#
#     for index in range(len(word_array) - 1):
#         if word_array[index + 1] > word_array[index]:
#             continue
#         else:
#             print "the rotation word is: ", word_array[index + 1]
#             return index + 1


# O(log(N))
def word_rotation(word_array):
    if len(word_array) <= 1:
        return word_array[0]

    limit_left = word_array[0]
    arr_len = len(word_array)
    mid_point = arr_len // 2

    if word_array[mid_point] < limit_left: # on right side
        print "smaller than first: ",word_array[mid_point]
        if word_array[mid_point - 1] > word_array[mid_point]: # check if before it is greater, then found
            return word_array[mid_point]
        return word_rotation(word_array[:mid_point])
    else:
        print "greater than first: ",word_array[mid_point]
        print "next: ",word_array[mid_point + 1]
        if word_array[mid_point] > word_array[mid_point + 1]:
            print word_array[mid_point] + "greater than" + word_array[mid_point + 1]
            return word_array[mid_point + 1]
        return word_rotation(word_array[mid_point + 1:])



words_1 = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

words_2 = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'xgotl',
    'yaotl',
    'yuahfs',
    'zzzzz',
    'appmptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage'
]



print word_rotation(words_2)

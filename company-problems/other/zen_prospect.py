# Complete the function below.
from math import sqrt


def perfect_check(input_str):
    num = int(input_str, 16)
    return sqrt(num).is_integer()

perfect_pieces = []
# def getMin(s, cut = 1, pieces = []):
#     # if s[0] is p.s., pass spliced s in getMin and find min, s. when done, append to perfect pieces
#     print "pieces is: ",pieces
#     if cut == len(s):
#         print "we have reached the end: ",cut
#         return
#     if not perfect_check(s[:cut]):
#         print "our substring isn't perfect: ",s[:cut]
#         return getMin(s, cut + 1, pieces)
#     else:
#         print "our substring is perfect: ",s[:cut]
#         pieces.append(s[:cut])
#         return getMin(s[cut:], 1, pieces)
#     return pieces

def getMin(s, cut = None, pieces = []):
    print "cut is: ",cut
    if cut == None:
        print "cut is none"
        cut = len(s)
        print "cut is: ",cut

    if s[:cut] == '':
        return ''.join(pieces)

    if not perfect_check(s[:cut]):
        print "our substring isn't perfect: ",s[:cut]
        return getMin(s, cut - 1, pieces)

    if perfect_check(s[:cut]):
        print "our substring is perfect: ",s[:cut]
        pieces.append(s[:cut])
        return getMin(s[cut:], len(s), pieces)

# print getMin("1a919")
print getMin("896bb1")

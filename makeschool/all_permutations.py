# Return all permutations of list of elements

# Python function to print permutations of a given list
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]

       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]

       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                print 'i: ',i
                print perm[:i]
                print elements[0:1]
                print perm[i:]
                yield perm[:i] + elements[0:1] + perm[i:]

def permutations(head, tail=''):
    if len(head) == 0: print tail
    else:
        for i in range(len(head)):
            print 'head[0:i]: ',head[0:i]
            print 'head[i+1:]',head[i+1:]
            print 'tail+head[i]',tail+head[i]
            permutations(head[0:i] + head[i+1:], tail+head[i])

# Driver program to test above function
data = list('CAMPBELL')
# for p in permutation(data):
#     print p
# print all_perms([1,2,3])
print permutations(['a','b','c'])
# for p in all_perms([1,2,3]):
#     print p

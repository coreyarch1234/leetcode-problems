# Determine whether one string appears within another string in reversed order.
# contains_reversed('super bowl', 'wob') => True
# contains_reversed('super bowl', 'owl') => False

def reverse_contains(str1, str2): # str2 reversed in str1
    return str2[::-1] in str1

print reverse_contains('superbowl', 'wob')
print reverse_contains('super bowl', 'owl')

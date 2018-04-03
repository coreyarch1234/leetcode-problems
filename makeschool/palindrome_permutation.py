# Write an efficient function that checks whether any permutation of an input string is a palindrome.
# permutation_palindrome('civic') => True
# permutation_palindrome('vicic') => True
# permutation_palindrome('civil') => False

# for palindrome, there has to be pairs of same letters with at most, 1 unique
def permutation_palindrome(input_str):
    str_set = set()
    # insert letters in set if they do not exist. check length after iterate whole string
    for letter in input_str:
        if letter in str_set:
            str_set.remove(letter)
        else:
            str_set.add(letter)
    return len(str_set) <= 1

print permutation_palindrome('civic') #=> True
print permutation_palindrome('vicic') #=> True
print permutation_palindrome('civil') #=> False
print permutation_palindrome('mmo') #=> True
print permutation_palindrome('yakak') #=> True
print permutation_palindrome('travel') #=> False

# def say_hello():
#     print 'Hello, World'

# for i in xrange(5):
#     say_hello()



# Write a function that takes in a string and identifies the longest palindrome in that string through any combination of the letters.

# It doesn't need to be real words, the order of the letters does not matter and you can return back any variation of the word which is a palindrome as long as it is the longest.

# You can use any language of your choice.

# Examples:
# racecar -> racecar || craearc || [other variations]
# racecarff -> racfefcar || fcraearcf || [other variations]
# abbccc -> bcccb || bcacb || [other variations]
# cb c  bc

def generate_string(str, letter):
    str_arr = list(str)
    str_arr.append(letter)#end
    str_arr.insert(0, letter) #start
    return  ''.join(str_arr)


def longest_palindrome(str):
    letter_dict = {}
    for letter in str:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    palindrome = ''

    used_all = False
    while used_all is False:
        used_all = True
        for letter in letter_dict.keys():
            if letter_dict[letter] >= 2:
                palindrome = generate_string(palindrome, letter)
                letter_dict[letter] -= 2
                used_all = False

    # insert letter in middle of string
    len_palindrome = len(palindrome)
    for letter in letter_dict.keys():
        if letter_dict[letter] > 0:
            palindrome = palindrome[:(len_palindrome / 2)] + letter + palindrome[(len_palindrome / 2):]
            return palindrome


input_s = 'abbccc'
input_s2 = 'racecar'
input_s3 = 'racfefcar'
print longest_palindrome(input_s3)

# print generate_string('bb', 'c')

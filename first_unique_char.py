# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#first dict, key is letter, value is freq,
#then run through strin gand find which key value is correct and return index,

def firstUniqChar(s): # O(n)
        """
        :type s: str
        :rtype: int
        """
        letter_freq = {}
        for letter in s: #run time O(n)
            if letter not in letter_freq:
                letter_freq[letter] = 1
            else:
                letter_freq[letter] += 1

        for index, letter in enumerate(s): # O(n)
            if letter_freq[letter] == 1:
                return index
        return -1

print firstUniqChar("leetcode")
print firstUniqChar("loveleetcode")
print firstUniqChar("d")

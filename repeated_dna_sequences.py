# https://leetcode.com/problems/repeated-dna-sequences/description/
#
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].

def findRepeatedDnaSequences(self, s):
    l, r = [], []
    if len(s) < 10: return []
    for i in range(len(s) - 9):
        l.extend([s[i:i + 10]])
    return [k for k, v in collections.Counter(l).items() if v > 1]

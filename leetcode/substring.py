# def get_substrings(input_s):
#     s_len = len(input_s)
#     substring_list = []
#     for i in range(s_len):
#         for j in range(i, s_len):
#             substring_list.append(input_s[i:j + 1])
#     return substring_list
#
# print get_substrings('abcde')
# print get_substrings('123')

# def palindrome(sing):
#     palindrome_set = set()
#     all_subsings = get_subsings(sing)
#     for subsing in all_subsings:
#         if subsing == subsing[::-1]:
#             palindrome_set.add(subsing)
#     return len(palindrome_set)

# def palindrome(s):
#     palindrome_set = set()
#     s_length = len(s)
#     for idx, char in enumerate(s):
#         # check for single letters
#         palindrome_set.add(char)
#         # Check for longest odd palindrome(s)
#         start, end = idx - 1, idx + 1
#         while start >= 0 and end < s_length and s[start] == s[end]:
#             palindrome_set.add(s[start:end+1])
#             start -= 1
#             end += 1
#
#         # Check for longest even palindrome(s)
#         start, end = idx, idx + 1
#         while start >= 0 and end < s_length and s[start] == s[end]:
#             palindrome_set.add(s[start:end+1])
#             start -= 1
#             end += 1
#
#     return len(palindrome_set)

# print palindrome('aabaa')



def maxLength(a, k):
    current = []
    max_len = -1
    for i in a:
        current.append(i)
        while sum(current) > k:
           current = current[1:]
        if sum(current) <= k:
            max_len = max(max_len, len(current))

    return max_len

print maxLength([1,2,3], 3)

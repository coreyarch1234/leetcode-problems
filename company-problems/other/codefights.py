# import re
# def shortestSolutionLength(source):
#     # increment counter of length
#     # don't count spaces
#     # create bool for block comment when start (true), when end, (false) and don't increment anything in between
#     # when line comment seen, skip to next line
#
#     total_length = 0
#     new_lines = []
#     for line in source:
#         new_lines.append(re.sub('/\*(.|\n)*?\*/', '', line))
#     new_lines = [''.join(new_lines)]
#     # return new_lines
#     for line in new_lines:
#         for index in range(len(line)):
#             if line[index] == '/' and index + 1 <= len(line) - 1 and line[index + 1] == '/':
#                 break
#             if line[index] != ' ':
#                 total_length += 1
#     return total_length
#     #
#     # s = "int b = 47;/*37;*///41;"
#     # a = "int c = 3/*4//5*/;"
#     # new_s = re.sub('/\*(.|\n)*?\*/', '', s)
#     # new_a = re.sub('/\*(.|\n)*?\*/', '', a)
#     # new_b = re.sub('/[^/]*$', '', 'apple//44')
#     # return new_b
#
# print shortestSolutionLength(["int a = 2;",
#           "int b = 47;/*37;*///41;",
#           "int c = 3/*4//5*/;",
#           "return a / b * c/*a /* b / c*/;"])
#
# # print shortestSolutionLength(["var a = 2;",
# #  "/*",
# #  "var b = 2;",
# #  "if (a === b) {",
# #  "  b = a + 1;",
# #  "  //b = a * 2 - 1;",
# #  "}",
# #  "*/",
# #  "var b = 3;",
# #  "return a * b;"])

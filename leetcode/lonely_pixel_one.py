#
# Given a picture consisting of black and white pixels, find the number of black lonely pixels.
#
# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.
#
# A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.
#
# Example:
# Input:
# [['W', 'W', 'B'],
#  ['W', 'B', 'W'],
#  ['B', 'W', 'W']]
#
# Output: 3
# Explanation: All the three 'B's are black lonely pixels.


def findLonelyPixel(picture): # O(N^2)
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        black_white_dict = {'W': 0, 'B': -1}
        row_sum_list = []
        col_sum_list = []
        num_of_rows = len(picture)
        num_of_cols = len(picture[0])

        lonely_bp_count = 0

        # calculate sum of rows
        for i in range(num_of_rows):
            row_sum = 0
            for j in range(num_of_cols):
                letter = picture[i][j]
                row_sum += black_white_dict[letter]
            row_sum_list.append(row_sum)
        # print 'row_sum_list',row_sum_list

        for j in range(num_of_cols):
            col_sum = 0
            for i in range(num_of_rows):
                letter = picture[i][j]
                col_sum += black_white_dict[letter]
            col_sum_list.append(col_sum)
        # print 'col_sum_list',col_sum_list

        for i in range(num_of_rows):
            for j in range(num_of_cols):
                if picture[i][j] == 'B':
                    if row_sum_list[i] == -1 and col_sum_list[j] == -1:
                        lonely_bp_count += 1
                    else:
                        continue
        # print 'lonely_bp_count: ',lonely_bp_count

        return lonely_bp_count

# https://www.getpy.com/hashtable/challenge?tastiest-meal
#
#
# Tastiest Meal
# You are in Venice for vacation. There are k restaurants in town. You eat at one of them each day and each serves a different meal every day. You need to find the most enjoyment you can get over n days eating at these restaurants.
#
# The restaurant meals are a n by k array of arrays of numbers, where meals[i][j] represents the enjoyment you would get on day i eating at restaurant j.
#
# Example input:
#
# [[1, 2, 3],
#  [5, 1, 2],
#  [3, 9, 6]]
# Output:
#
# 17
# Explanation:
#
# One day 0, you eat a restaurant 2. Enjoyment: 3
# One day 1, you eat a restaurant 0. Enjoyment: 5
# One day 2, you eat a restaurant 1. Enjoyment: 9
# Total Enjoyment: 17

# TIME : 6 min

def solution(meals):
    # Type your solution here
    max_enjoyment = 0
    for day_enjoyment in meals:
        max_enjoyment += max(day_enjoyment)
    return max_enjoyment

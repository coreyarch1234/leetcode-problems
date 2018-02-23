# Writing programming interview questions hasn't made me rich. Maybe trading Apple stocks will.
#
# Suppose we could access yesterday's stock prices as a list, where:
#
# The indices are the time in minutes past trade opening time, which was 9:30am local time.
# The values are the price in dollars of Apple stock at that time.
# So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.
#
# Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
#
# For example:
#
#   stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
#
# get_max_profit(stock_prices_yesterday)
# # returns 6 (buying for $5 and selling for $11)
#
# No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).






# O(N^2) solution
# def get_max_profit(stock_prices):
#     profit_dict = {}
#     max_profit = 0
#     for index, price in enumerate(stock_prices):
#         profit_dict[price] = []
#         for other_price in stock_prices[index:]:
#             if other_price > price:
#                 profit_dict[price].append(other_price)

#     for key, price in profit_dict.items():
#         for profit in profit_dict[key]:
#             if profit - key > max_profit:
#                 max_profit = profit - key
#     return profit_dict



# O(N) solution
# def get_max_profit(stock_prices):
#     curr = stock_prices[0]
#     length_stock = len(stock_prices)
#     reached_increase = False
#     start_index = 0
#     for index, price in enumerate(stock_prices):
#         if price > curr:
#             start_index = index - 1
#             reached_increase = True
#             break
#         else:
#             curr = price
#     # print "start index is: ",start_index
#     if reached_increase == False:
#         return stock_prices[length_stock - 1] - stock_prices[length_stock - 2]

#     stock_prices = stock_prices[start_index:]
#     # print "new stock prices: ",stock_prices
#     max_arr = 0
#     curr_max = 0
#     curr_diff = 0
#     curr_price = stock_prices[0]
#     for price in stock_prices[1:]:
#         if curr_diff + (price - curr_price) > 0:
#             curr_diff += price - curr_price
#             # print "curr diff: ",curr_diff
#             # print "curr_max: ",curr_max
#             # print
#             if curr_diff > curr_max:
#                 curr_max = curr_diff
#         else:
#             if curr_max > max_arr:
#                 max_arr = curr_max
#                 curr_diff = 0
#                 curr_max = 0
#         curr_price = price
#         # print "curr max: ",curr_max

#     if curr_max > max_arr:
#         max_arr = curr_max

#     # print "max arr: ",max_arr
#     return max_arr

# their solution
def get_max_profit(stock_prices_yesterday):

    if len(stock_prices_yesterday) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price  = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    # start at the second (index 1) time
    # we can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # if we started at index 0, we'd try to buy *and* sell at time 0.
    # this would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in xrange(1, len(stock_prices_yesterday)):
        current_price = stock_prices_yesterday[current_time]

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit





# add some more tests

test_input = [10, 7, 5, 8, 11, 9]
test_input_2 = [100, 50, 25, 6, 2]
test_input_3 = [10, 7, 5, 8, 11, 9, 12, 2, 3, 13]
test_input_4 = [10, 7, 5, 8, 11, 9, 12, 2, 3, 1000, 1000, 400, 32121, 600 ]

print get_max_profit(test_input_4)

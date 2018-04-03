# Space O(N)
# Time O(N)
# def reorder(data, order):
    # order_dict = {}
    # result = [''] * len(data)
    # for index, place in enumerate(order):
    #     order_dict[place] = data[index]
    # print order_dict
    #
    # for place in range(len(data)):
    #     result[place] = order_dict[place]
    # print 'result is: ',result

# Space O(N)
# Time O(N)
# def reorder(data, order):
#         order_dict = {}
#         for index, place in enumerate(order):
#             order_dict[place] = data[index]
#         print order_dict
#
#         for place in range(len(data)):
#             order[place] = order_dict[place]
#         print 'result is: ',order

def reorder(data, order):
        result = [''] * len(order)
        for index, place in enumerate(order):
            result[place] = data[index]
        return result


data = ['E', 'A', 'D', 'B', 'C']
order = [4, 0, 3, 1, 2]
print reorder(data, order)

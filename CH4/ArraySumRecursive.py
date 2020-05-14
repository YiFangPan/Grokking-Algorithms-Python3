# 4-9, Practice 4.1

# def sum(arr):
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return arr.pop(0) + sum(arr)

# Book Solution
def sum(list):
    if list == []:
        return 0
    else:
        # list[1:] => slice, from index 1 to end
        return list[0] + sum(list[1:])


test_array = [2, 4, 6]

print(sum(test_array))
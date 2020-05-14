def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr.pop(0) + sum(arr)

test_array = [2, 4, 6]

print(sum(test_array))
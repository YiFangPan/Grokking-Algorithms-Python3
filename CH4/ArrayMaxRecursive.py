# 4-9, Practice 4.3

def max(list):
    if len(list) == 1:
        return list[0]
    if list[0] < list[1]:
        return max(list[1:])
    if list[0] > list[1]:     
        arr = list[1:]
        arr.append(list[0])
        return max(arr)

test_list = [2, 5, 11, 9, 6]

print(max(test_list))
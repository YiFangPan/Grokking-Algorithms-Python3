# 4-9, Practice 4.2

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

test_list = [1, 2, 3, 4, 5]

print(count(test_list))
def getSmallestIndex(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest_index = getSmallestIndex(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


test_array = [100, 30, 60, 20, 10]

print(selectionSort(test_array))
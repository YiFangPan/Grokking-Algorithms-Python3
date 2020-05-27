# 9-23

import numpy as np

compare_string1 = "FISH"
compare_string2 = "HISH"

# Generate mulitple array by string1 and string2 length
array = np.zeros((len(compare_string1),len(compare_string2)), dtype=int)

# Compare
for i in range(1, len(compare_string1)):
    for j in range(1, len(compare_string2)):
        if(compare_string1[i] == compare_string2[j]):
            array[i][j] = array[i-1][j-1] + 1
        else:
            array[i][j] = 0

print(array)

print(np.max(array))
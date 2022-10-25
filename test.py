# Input: arr[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
# Output: 6
# Explanation: The structure is like below.
# Trap “1 unit” between first 1 and 2, “4 units” between
# first 2 and 3 and “1 unit” between second last 1 and last 2

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
prefixsum=[0, 1, 1, 3, 4, 4, 5, 8, 10, 11, 13, 14]

water=[]
for i in arr:
    if arr[i]>arr[i+1]:
        print(arr[i],">",arr[i+1])
        if arr[i+2]>arr[i]:
            print(arr[i+2],">",arr[i])
            if arr[i+2]>arr[i]:
                print(arr[i])
            else:
                print(arr[i+2])


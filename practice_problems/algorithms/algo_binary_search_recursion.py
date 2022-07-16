# Binary Search using recursion method


def binarySearch(arr, low, high, element):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            return binarySearch(arr, low, mid-1, element)
        else:
            return binarySearch(arr, mid+1, high, element)
    else:
        return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

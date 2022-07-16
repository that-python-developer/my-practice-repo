# Binary Search using iteration method
# Iteration can be used to repeatedly execute a set of statements without the overhead
# of function calls and without using stack memory.
# Iteration is faster and more efficient than recursion.


def binarySearch(arr, low, high, element):
    while high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            high = mid-1
        else:
            low = mid+1
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

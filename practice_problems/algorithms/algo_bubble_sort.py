# Bubble sort in Python
# Time Complexity - O(n^2)
# The worst-case condition for bubble sort occurs when elements of the array are arranged in decreasing order.

def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements (here we use as we have to traverse only till (len(arr) - 1)th index
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
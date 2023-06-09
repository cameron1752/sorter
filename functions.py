# bubble sort function
def bubble_sort(numArr):
    print("bubble sort started :)")
    n = len(numArr)

    isSwapped = False

    for i in range(n-1):
        for j in range (0, n-i-1):
            if numArr[j] > numArr[j + 1]:
                isSwapped = True
                numArr[j], numArr[j + 1] = numArr[j + 1], numArr[j]
        if not isSwapped:
            return

#selection sort function
def selection_sort(numArr):
    print("selection sort started :)")
    size = len(numArr)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if numArr[j] < numArr[min_index]:
                min_index = j
        (numArr[ind], numArr[min_index]) = (numArr[min_index], numArr[ind])

# function to check the (hopefully) sorted array
def check_sort(numArr):
    for x in range(len(numArr)):
        if x > 0:
            if numArr[x] < numArr[x-1]:
                return -1
    return 0
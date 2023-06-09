import time
# bubble sort function
def bubble_sort(numArr, drawData, speed):
    n = len(numArr)

    isSwapped = False

    for i in range(n-1):
        for j in range (0, n-i-1):
            if numArr[j] > numArr[j + 1]:
                isSwapped = True
                numArr[j], numArr[j + 1] = numArr[j + 1], numArr[j]
                drawData(numArr, ["#F7E806" if x == j or x == j+1 else "#4204CC" for x in range(len(numArr))])
                time.sleep(speed)
                
        if not isSwapped:
            return

#selection sort function
def selection_sort(numArr, drawData, speed):
    size = len(numArr)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if numArr[j] < numArr[min_index]:
                min_index = j
        (numArr[ind], numArr[min_index]) = (numArr[min_index], numArr[ind])
        drawData(numArr, ["#F7E806" if x == j or x == j+1 else "#4204CC" for x in range(len(numArr))])
        time.sleep(speed)


# quick sort function
def partition(numArr, low, high, drawData, speed):
    pivot = numArr[high]

    i = low - 1

    for j in range(low, high):
        if numArr[j] <= pivot:
            i = i + 1

            (numArr[i], numArr[j]) = (numArr[j], numArr[i])
            drawData(numArr, ["#F7E806" if x == j or x == j+1 else "#4204CC" for x in range(len(numArr))])
            time.sleep(speed)

    (numArr[i + 1], numArr[high]) = (numArr[high], numArr[i + 1])
    drawData(numArr, ["#F7E806" if x == j or x == j+1 else "#4204CC" for x in range(len(numArr))])
    time.sleep(speed)

    return i + 1

def quick_sort(numArr, low, high, drawData, speed):

    if low < high:
        pi = partition(numArr, low, high, drawData, speed)

        quick_sort(numArr, low, pi - 1, drawData, speed)

        quick_sort(numArr, pi + 1, high, drawData, speed)

# function for merge sort
def merge(numArr, l, m, r, drawData, speed):
    n1 = m - l + 1
    n2 = r - m
    
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = numArr[l + i]

    for j in range(0, n2):
        R[j] = numArr[m + 1 + j]
    
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            numArr[k] = L[i]
            drawData(numArr, ["#F7E806" if x == j or x == j+1 else "#4204CC" for x in range(len(numArr))])
            time.sleep(speed)
            i += 1
        else:
            numArr[k] = R[j]
            drawData(numArr, ["#F7E806" if x == j or x == j+1 else "#4204CC" for x in range(len(numArr))])
            time.sleep(speed)
            j += 1
        k += 1
    
    while i < n1:
        numArr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        numArr[k] = R[j]
        j += 1
        k += 1

def merge_sort(numArr, l, r, drawData, speed):
    if l < r:
        m = l+(r-l)//2

        merge_sort(numArr, l, m, drawData, speed)
        merge_sort(numArr, m+1, r, drawData, speed)
        merge(numArr, l, m, r, drawData, speed)


# function to check the (hopefully) sorted array
def check_sort(numArr):
    for x in range(len(numArr)):
        if x > 0:
            if numArr[x] < numArr[x-1]:
                return -1
    return 0
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





# function to check the (hopefully) sorted array
def check_sort(numArr):
    for x in range(len(numArr)):
        if x > 0:
            if numArr[x] < numArr[x-1]:
                return -1
    return 0
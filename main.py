import random
import time
from functions import bubble_sort
from functions import check_sort
from functions import selection_sort

# main block here
numArr = []
numArr = [random.randint(0,10000) for i in range(5)]

numArrBubble = []
numArrSelection = []

numArrBubble = numArr.copy()
numArrSelection = numArr.copy()

# print(numArr)
# print(numArrBubble)
# print(numArrSelection)

startTime = time.time()

bubble_sort(numArrBubble)

if check_sort(numArrBubble) == 0:
    print("Array sorted")
else:
    print("Array not sorted")

print((time.time() - startTime)*1000, " ms")

# print(numArr)
# print(numArrBubble)
# print(numArrSelection)

startTime = time.time()

selection_sort(numArrSelection)

if check_sort(numArrSelection) == 0:
    print("Array sorted")
else:
    print("Array not sorted")

print((time.time() - startTime)*1000, " ms")


# print(numArr)
# print(numArrBubble)
# print(numArrSelection)
        
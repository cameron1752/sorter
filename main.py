import random
import time
import sys
from functions import bubble_sort
from functions import check_sort
from functions import selection_sort
from functions import quick_sort

if len(sys.argv) > 1:
    size = int(sys.argv[1])
else:
    size = 5000

# main block here
numArr = []
numArr = [random.randint(0,size*4) for i in range(size)]

numArrBubble = []
numArrSelection = []
numArrQuick = []

numArrBubble = numArr.copy()
numArrSelection = numArr.copy()
numArrQuick = numArr.copy()

# print(numArr)
# print(numArrBubble)
# print(numArrSelection)
# print (numArrQuick)

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
# print (numArrQuick)

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
# print (numArrQuick)


startTime = time.time()

quick_sort(numArrQuick, 0, len(numArrQuick) - 1)

if check_sort(numArrQuick) == 0:
    print("Array sorted")
else:
    print("Array not sorted")

print((time.time() - startTime)*1000, " ms")

# print(numArr)
# print(numArrBubble)
# print(numArrSelection)
# print (numArrQuick)
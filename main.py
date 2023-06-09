import random
import time
import sys
import wx
from functions import bubble_sort
from functions import check_sort
from functions import selection_sort
from functions import quick_sort
from gui import MyFrame

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

print("bubble sort started :)")
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

print("selection sort started :)")
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

print("quick sort started :)")
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

app = wx.App()
frame = MyFrame()
app.MainLoop()
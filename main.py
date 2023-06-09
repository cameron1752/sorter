import random

def bubble_sort():
    print("bubble sort started :)")


# function to check the (hopefully) sorted array
def check_sort(numArr):
    for x in range(100):
        if x > 0:
            if numArr[x] < numArr[x-1]:
                return -1
    return 0
            





print("hello beotch")
numArr = []
numArr = [random.randint(0,1000) for i in range(100)]

for x in range(100):
    print(numArr[x])

if check_sort(numArr) == 0:
    print("Array sorted")
else:
    print("Array not sorted")
        
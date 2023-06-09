import random
import time
import sys
import wx
from tkinter import *
from tkinter import ttk
from functions import bubble_sort
from functions import check_sort
from functions import selection_sort
from functions import quick_sort
from functions import merge_sort
from gui import MyFrame

window = Tk()
window.title("Sorter")
window.maxsize(2160, 1440)
window.config(bg = "#FFFFFF")

if len(sys.argv) > 1:
    size = int(sys.argv[1])
else:
    size = 100

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Selection Sort', 'Quick Sort', 'Merge Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


def drawData(data, color):
    canvas.delete("all")
    canvas_width = 1500
    canvas_height = 850
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])

    window.update_idletasks()

def generate():
    # main block here
    global numArr
    numArr = [random.randint(0,size*4) for i in range(size)]
    
    drawData(numArr, ["#4204CC" for x in range(len(numArr))])

def sort():
    if check_sort(numArr) == 0:
        generate()


    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(numArr, drawData, set_speed())
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(numArr, drawData, set_speed())
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(numArr, 0, len(numArr) - 1, drawData, set_speed())
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(numArr, 0, len(numArr) - 1, drawData, set_speed())

    drawData(numArr, ["#4204CC" for x in range(len(numArr))])


UI_frame = Frame(window, width= 1600, height=900, bg="#FFFFFF")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select sorting algorithm 
l1 = Label(UI_frame, text="Algorithm: ", bg="#FFFFFF")
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed 
l2 = Label(UI_frame, text="Sorting Speed: ", bg="#FFFFFF")
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# sort button 
b1 = Button(UI_frame, text="Sort", command=sort, bg="#C4C5BF")
b1.grid(row=2, column=1, padx=5, pady=5)

# button for generating array 
b3 = Button(UI_frame, text="Generate Array", command=generate, bg="#C4C5BF")
b3.grid(row=2, column=0, padx=5, pady=5)

# canvas to draw our array 
canvas = Canvas(window, width=1500, height=850, bg="#FFFFFF")
canvas.grid(row=1, column=0, padx=10, pady=5)

window.mainloop()
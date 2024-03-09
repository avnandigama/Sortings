import tkinter as tk
import random

def swap(pos_0, pos_1):
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21-bar11, 0)
    canvas.move(pos_1, bar12-bar22, 0)

def animate():
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(500, animate) 
        except StopIteration:
            worker = None

worker = None

def bubble_sort():
    global barList
    global lengthList

    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if lengthList[j] > lengthList[j + 1]:
                lengthList[j], lengthList[j + 1] = lengthList[j + 1], lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1], barList[j]
                swap(barList[j + 1], barList[j])
                yield

def generate():
    global barList
    global lengthList
    canvas.delete('all')
    barstart = 50
    barwidth = 20
    barList = []
    lengthList = []

    heights = [int(x) for x in entry.get().split()]
    for height in heights:
        bar = canvas.create_rectangle(barstart, 365 - height, barstart + barwidth, 365, fill='black')
        barList.append(bar)
        barstart += barwidth + 5
        lengthList.append(height)


def on_sort():
    generate()
    global worker
    worker = bubble_sort()
    animate()

window = tk.Tk()
window.title('Bubble Sorting Visualization')
window.geometry('1200x650')

canvas = tk.Canvas(window, width='1200', height='400')
canvas.grid(column=0, row=0, columnspan=20)

entry = tk.Entry(window)
entry.grid(column=1, row=1)

button_shuf = tk.Button(window, text='Display', command=generate)
button_shuf.grid(column=2, row=1)

button = tk.Button(window, text='Sort', command=on_sort)
button.grid(column=3, row=1)

window.mainloop()

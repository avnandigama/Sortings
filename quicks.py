import tkinter as tk
import time

def quick_sort(arr, canvas, low, high):
    if low < high:
        pi = partition(arr, canvas, low, high)
        quick_sort(arr, canvas, low, pi - 1)
        quick_sort(arr, canvas, pi + 1, high)

def partition(arr, canvas, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_bars(canvas, arr, swap1=i, swap2=j)
            time.sleep(0.1)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_bars(canvas, arr, swap1=i + 1, swap2=high)
    time.sleep(0.1)

    return i + 1

def draw_bars(canvas, arr, swap1=None, swap2=None):
    canvas.delete("all")
    canvas_height = 300
    canvas_width = 500
    num_bars = len(arr)
    gap = 20 
    bar_width = (canvas_width - (gap * (num_bars - 1))) / num_bars
    max_height = max(arr)

    for i in range(len(arr)):
        normalized_height = (arr[i] / max_height) * canvas_height
        color = "black"

        canvas.create_rectangle(
            i * (bar_width + gap),
            canvas_height - normalized_height,
            (i + 1) * (bar_width + gap),
            canvas_height,
            fill=color
        )

    window.update_idletasks()
    window.update()

def generate_from_input():
    global array
    array = [int(x) for x in entry.get().split()]
    draw_bars(canvas, array)

window = tk.Tk()
window.title('Quick Sort Visualization')
window.geometry('1200x650')

canvas = tk.Canvas(window, width='1200', height='400')
canvas.grid(column=0, row=0, columnspan=20)

entry = tk.Entry(window)
entry.grid(column=1, row=1)

dbutton = tk.Button(window, text="Display", command=generate_from_input)
dbutton.grid(column=2, row=1)

button = tk.Button(window, text="Quick Sort", command=lambda: quick_sort(array, canvas, 0, len(array) - 1))
button.grid(column=3, row=1)

window.mainloop()

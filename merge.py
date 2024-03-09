import tkinter as tk
import time
def merge_sort(arr, canvas):
    merge_sort_helper(arr, canvas, 0, len(arr) - 1)

def merge_sort_helper(arr, canvas, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_helper(arr, canvas, start, mid)
        merge_sort_helper(arr, canvas, mid + 1, end)
        merge(arr, canvas, start, mid, end)

def merge(arr, canvas, start, mid, end):
    left_arr = arr[start:mid + 1]
    right_arr = arr[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        draw_bars(canvas, arr)
        time.sleep(0.1)  
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        draw_bars(canvas, arr)
        time.sleep(0.1) 
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        draw_bars(canvas, arr)
        time.sleep(0.1) 
        j += 1
        k += 1

def draw_bars(canvas, arr):
    canvas.delete("all")
    canvas_height = 300
    canvas_width = 500
    num_bars = len(arr)
    bar_width = (canvas_width - 20) / num_bars  
    max_height = max(arr)

    for i in range(num_bars):
        normalized_height = (arr[i] / max_height) * (canvas_height - 20)  
        canvas.create_rectangle(
            i * bar_width + 20, 
            canvas_height - normalized_height,
            (i + 1) * bar_width + 10, 
            canvas_height,
            fill="black"
        )

    window.update_idletasks()
    window.update()

def start_merge_sort():
    arr = [int(x) for x in entry.get().split()]  
    merge_sort(arr, canvas)

window = tk.Tk()
window.title('Bubble Sorting Visualization')
window.geometry('1200x650')

canvas = tk.Canvas(window, width='1200', height='400')
canvas.grid(column=0, row=0, columnspan=20)

entry = tk.Entry(window)
entry.grid(column=1, row=1)

dbutton = tk.Button(window, text="Display", command=lambda: draw_bars(canvas, [int(x) for x in entry.get().split()]))
dbutton.grid(column=2, row=1)

button = tk.Button(window, text="Merge Sort", command=start_merge_sort)
button.grid(column=3, row=1)

window.mainloop()
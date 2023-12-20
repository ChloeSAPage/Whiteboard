import tkinter as tk
from tkinter.colorchooser import askcolor


def start_drawing(event):
    global is_drawing, prev_x, prev_y
    is_drawing = True
    prev_x, prev_y = event.x, event.y


def draw(event):
    global is_drawing, prev_x, prev_y
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(prev_x, prev_y, current_x, current_y,
                           fill=drawing_color, width=line_width, capstyle=tk.ROUND, smooth=True)
        prev_x, prev_y = current_x, current_y


def stop_drawing(event):
    global is_drawing
    is_drawing = False


def change_pen_color():
    global drawing_color
    color = askcolor()[1]
    if color:
        drawing_color = color


def change_line_width(value):
    global line_width
    line_width = int(value)


# Create the Window
window = tk.Tk()
window.title("Whiteboard App")

canvas = tk.Canvas(window, bg="white")
canvas.pack(fill="both", expand=True)

is_drawing = False
drawing_color = "black"
line_width = 2

window.geometry("800x600")

window.mainloop()
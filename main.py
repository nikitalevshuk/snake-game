import tkinter
import random
import os


ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

window = tkinter.Tk()
window.title('Snake')
window.resizable(width=False, height=False)

canvas = tkinter.Canvas(
    window, bg = 'black',
    width = WINDOW_WIDTH,
    height = WINDOW_HEIGHT,
    borderwidth = 0,
    highlightthickness=0
)
canvas.pack()
window.update()

window.mainloop()
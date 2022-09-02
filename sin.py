from tkinter import *
from math import radians, sin, cos, tan
import math

root = Tk()

c1 = Canvas(root, height=720, width = 900)
c1.pack()

ix = iy= 0

for x in range(2880):
    x = radians(x)
    y = 360 - 100 * sin(x)
    c1.create_line(ix*20, iy, x*20, y)
    c1.update()
    ix = x
    iy = y

ix = iy= 0

for x in range(2880):
    x = radians(x)
    y = 360 - 100 * cos(x)
    c1.create_line(ix*20, iy, x*20, y)
    c1.update()
    ix = x
    iy = y

ix = iy= 0

for x in range(2880):
    x = radians(x)
    y = 360 - 100 * tan(x)
    c1.create_line(ix*20, iy, x*20, y)
    c1.update()
    ix = x
    iy = y


root.mainloop()
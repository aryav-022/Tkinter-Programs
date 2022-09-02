from tkinter import *

r = int(input("Enter Radius (less than 300): "))

root = Tk()

c1 = Canvas(root, height=600, width=600)
c1.pack()

ix = 50
iy = 300

for x in range(51, r*2 + 51):
    y = -(r**2 - (x - 300)**2)**0.5 + 300
    c1.create_line(ix, iy, x, y)
    c1.update()
    ix, iy = x, y

for x in range(r*2 + 50, 49, -1):
    y = (r**2 - (x - 300)**2)**0.5 + 300
    c1.create_line(ix, iy, x, y)
    c1.update()
    ix, iy = x, y

root.mainloop()
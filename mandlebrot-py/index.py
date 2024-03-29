import tkinter as tk
import numpy as np
import math

l = 1000

root = tk.Tk()
root.title("Mandlebrot")
root.geometry(f"{l}x{l}")
canvas = tk.Canvas(root, width=l, height=l)
canvas.pack()
img = tk.PhotoImage(width=l, height=l)

# Coordinate system with origin at center
def c(x, y):
    newy = 500 - y
    newx = 500 + x
    return (newx, newy)

# Scaled coordinate system ranging from -2 to 2
def d(x, y):
    newx = round(x * 250)
    newy = round(y * 250)
    return c(newx, newy)

def julia(z, C, depth):
    for _ in range(depth):
        z = z**2 + C
    return z

def is_stable(z):
    return abs(z) <= 3

def precise_mandlebrot(C, precision, initial_iterations):
    z = julia(complex(0, 0), C, 10)
    gradient = int(255 / precision)
    if abs(z) >= 2:
        return (False, (precision - initial_iterations) * gradient)
    else:
        for i in range(precision - initial_iterations):
            z = julia(z, C, 1)
            if abs(z) >= 2:
                return (False, i * gradient)
        return (True, 0)


for i in range(-499, 499):
    for j in range(-499, 499):

        x = i / 250
        y = j / 250
        
        # z = julia(complex(0, 0), complex(x, y), 10)
        # if is_stable(z):
        #     img.put("black", d(x, y))

        (is_stable, g) = precise_mandlebrot(complex(x, y), 20, 3)
        if is_stable:
            img.put("black", d(x, y))
        else:
            hex = f'#{g:02x}{g:02x}{g:02x}'
            img.put(hex, d(x, y))

        if x == 0:
            img.put("black", d(x, y))
        if y == 0:
            img.put("black", d(x, y))

        pythagoras = (x ** 2) + (y ** 2)
        if math.isclose(pythagoras, 1, rel_tol=0.005):
            img.put("black", d(x, y))

canvas.create_image((0, 0), image=img, anchor="nw")

root.mainloop()

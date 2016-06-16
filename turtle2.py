import turtle
n=int(input("ingrese un valor (entero): "))
t=turtle.Pen()
for x in range(0, n):
    t.forward(100)
    t.left(360/n)
    turtle.getscreen()._root_mainloop()
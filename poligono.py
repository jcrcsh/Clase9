import turtle
t=turtle.Pen()
def mipoligono(size):
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    turtle.getscreen()_.root.mainloop()

tam = int(input("ingrese un numero (2-100): "))
mipoligono(tam)


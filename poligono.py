import turtle
t=turtle.Pen()
def mipoligono(lados, tamLado):
    for x in range(1, 5):
        t.forward(tamLados)
        t.left(lado)
    turtle.getscreen()_.root.mainloop()

lados = int(input("ingrese un numero (2-100): "))
tamLado = int(input("ingrese la longitug de un lado: "))
mipoligono(lados, tamLado)


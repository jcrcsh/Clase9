from Tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 400, heght = 400)
canvas.pack()

myImage = PhotoImage(file = "ball.gif")
canvas.create_image(0, 0, anchor = NW, image = myImage)
tk.mainloop()
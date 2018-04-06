
#Here I have my turtle code
def prueba ():
    def house():

        tu.penup()
        tu.goto(0, -100)
        tu.pendown()

        # Parte cuadrada de la casa
        for i in range(4):
            # Cambio velocidad
            tu.speed(20)

            # Pongo la tortuga
            tu.shape("turtle")
            # Primero decido color del lápiz
            tu.pencolor("#E0E0E0")
            tu.forward(100)
            tu.left(90)
            tu.pensize(12)

        # Moviendo el cursor hacia un nuevo punto
        tu.penup()
        tu.goto(0, 0)
        tu.pendown()

        # Cambiando el color y el tamaño del lápiz
        tu.pensize(12)
        tu.pencolor("#FF9999")

        for i in range(3):
            # Techo de la casa
            tu.color("#FF9999")
            # Rellenar el triángulo que forma el techo de la casa
            tu.fillcolor("#FF9999")
            tu.begin_fill()
            tu.forward(100)
            tu.left(120)
            tu.end_fill()

    house()

    def tree1():
        # Tronco del arbol
        tu.penup()
        tu.goto(-150, -100)
        tu.pendown()
        tu.pensize(12)
        tu.pencolor("brown")

        tu.left(90)
        tu.forward(80)
        tu.left(90)
        tu.forward(10)
        tu.left(90)
        tu.forward(80)

        # Copa del arbol
        tu.penup()
        tu.goto(-185, 0)
        tu.pendown()
        tu.begin_fill()
        tu.fillcolor("green")
        tu.pensize(12)
        tu.pencolor("green")
        tu.circle(30)
        tu.end_fill()

    tree1()

    def tree2():
        # Tronco del arbol
        tu.penup()
        tu.goto(-300, -100)
        tu.pendown()
        tu.pensize(12)
        tu.pencolor("brown")
        tu.begin_fill()
        tu.fillcolor("brown")

        tu.right(180)
        tu.forward(100)
        tu.right(90)
        tu.forward(20)
        tu.right(90)
        tu.forward(100)
        tu.end_fill()

        # Copa del arbol
        tu.penup()
        tu.goto(-340, 20)
        tu.pendown()
        tu.begin_fill()
        tu.fillcolor("green")
        tu.pensize(12)
        tu.pencolor("green")
        tu.circle(50)
        tu.end_fill()

    tree2()

    def grass():
        # Base de cesped
        tu.penup()
        tu.goto(-350, -100)
        tu.pendown()
        tu.pensize(12)
        tu.pencolor("green")
        tu.left(90)
        tu.forward(500)

    grass()

    def window():
        # Cuadrado de la ventana

        tu.penup()
        tu.goto(60, -40)
        tu.pendown()
        tu.pensize(5)
        tu.pencolor("#E0E0E0")

        for i in range(4):
            tu.pencolor("#E0E0E0")
            tu.forward(20)
            tu.left(90)
            tu.pensize(5)

        # Primera division de la ventana
        tu.penup()
        tu.goto(70, -40)
        tu.pendown()
        tu.pensize(5)
        tu.pencolor("#E0E0E0")
        tu.left(90)
        tu.forward(20)

        # Segunda division de la ventana
        tu.penup()
        tu.goto(60, -30)
        tu.pendown()
        tu.pensize(5)
        tu.pencolor("#E0E0E0")
        tu.right(90)
        tu.forward(20)

    window()

    def sun():
        # Haciendo el sol
        tu.penup()
        tu.goto(220, 110)
        tu.pendown()
        tu.pensize(9)
        tu.pencolor("yellow")
        tu.begin_fill()
        tu.fillcolor("yellow")
        tu.circle(40)
        tu.end_fill()

    sun()

    def door():
        # Puerta de la casita
        tu.penup()
        tu.goto(70, -93)
        tu.pendown()
        tu.pensize(5)
        tu.pencolor("#E0E0E0")
        tu.begin_fill()
        tu.fillcolor("#E0E0E0")

        tu.left(90)
        tu.forward(40)
        tu.left(90)
        tu.forward(30)
        tu.left(90)
        tu.forward(40)
        tu.end_fill()

    door()

    def bird1():
        # Primer amago de pájaro
        tu.penup()
        tu.goto(-200, 120)
        tu.pendown()

        tu.pensize(7)
        tu.pencolor("#295ea4")

        tu.color("#295ea4")
        tu.fillcolor("#295ea4")
        tu.forward(20)
        tu.left(120)
        tu.forward(20)

    bird1()

    def bird2():
        # Segundo pájaro
        tu.penup()
        tu.goto(-250, 150)
        tu.pendown()

        tu.pensize(7)
        tu.pencolor("#295ea4")

        tu.color("#295ea4")
        tu.fillcolor("#295ea4")
        tu.right(120)
        tu.forward(20)
        tu.right(120)
        tu.forward(20)

    bird2()

    def bird3():
        # Tercer pájaro
        tu.penup()
        tu.goto(-300, 100)
        tu.pendown()

        tu.pensize(7)
        tu.pencolor("#295ea4")

        tu.color("#295ea4")
        tu.fillcolor("#295ea4")
        tu.right(180)
        tu.forward(20)
        tu.left(120)
        tu.forward(20)

    bird3()

    tu.penup()
    tu.goto(55, -100)
    tu.pendown()


from tkinter import *
import tkinter as tk
import turtle as tu


window = tk.Tk()

window.config(bg="blue")
#Change background colour

window.title("Mi tortuguita")
#Add window title

window.geometry('700x500')
#Resize window

canvas = tk.Canvas(master = window, width = 700, height = 300)
#Create canvas to show turtle function inside

canvas.pack(side=RIGHT, expand=FALSE)
#Relocate canvas to right, no expand

tu = tu.RawTurtle(canvas)
#Add turtle into canvas

prueba()
#Initiate drawing

#tk.Button(master = window, text ='Exit', command = exit()).pack(side = tk.BOTTOM)
#tk.Button(master = window, text = 'Repeat', command = prueba()).pack(side = tk.BOTTOM)
#Creates exit and repeat button

window.mainloop()













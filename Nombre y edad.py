#Fase 3: Nombre y edad
from tkinter import *
ventana = Tk()
Label(ventana,text="Nombre").pack()
nombre = Entry(ventana)
nombre.pack()
Label(ventana,text="Edad").pack()
edad = Entry(ventana)
edad.pack()
def guardar():

    print("Nombre:",nombre.get())
    print("Edad:",edad.get())
Button(
    ventana,
    text="Guardar",
    command=guardar
).pack()
ventana.mainloop()
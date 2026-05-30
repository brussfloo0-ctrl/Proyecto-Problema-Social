#Fase 6: Guardar en lista
from tkinter import *
ventana = Tk()
registros = []
nombre = Entry(ventana)
nombre.pack()
def guardar():

    registros.append(nombre)
Button(
    ventana,
    text="Guardar",
    command=guardar
).pack()
ventana.mainloop()
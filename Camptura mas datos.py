#Fase 2: captura nombre
from tkinter import *
ventana = Tk()
Label(ventana,text="Nombre").pack()
nombre = Entry(ventana)
nombre.pack()
def mostrar():
    print(nombre.get)
Button(
    ventana,
    text="Mostrar",
    command=mostrar
).pack()

ventana.mainloop()
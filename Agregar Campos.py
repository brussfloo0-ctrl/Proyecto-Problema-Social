#Fase 5: Agregar mas campos
from tkinter import *
ventana = Tk()
Label(ventana,text="Nombre").pack()
nombre = Entry(ventana)
nombre.pack()
Label(ventana,text="Edad").pack()
edad = Entry(ventana)
edad.pack()
Label(ventana,text="Sexo").pack()
sexo = Entry(ventana)
sexo.pack()
Label(ventana,text="Lugar").pack()
lugar = Entry(ventana)
lugar.pack()
def guardar():

    print(nombre.get())
    print(edad.get())
    print(sexo.get())
    print(lugar.get())
Button(
    ventana,
    text="Registrar",
    command=guardar
).pack()
ventana.mainloop()
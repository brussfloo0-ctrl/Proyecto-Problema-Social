#Fase 7: Mostrar registros en listbox
from tkinter import *
ventana = Tk()
registros = []
nombre = Entry(ventana)
nombre.pack()
lista = Listbox(ventana)
lista.pack()
def guardar():
    registros.append(nombre.get())
    lista.insert(
        END,
        nombre.get()
    )
Button(
    ventana,
    text="Registrar",
    command=guardar
).pack()
ventana.mainloop()
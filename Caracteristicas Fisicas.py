#Fase 4: Caracteristicas Fisicas
from tkinter import *
ventana = Tk()
Label(ventana,text="Estatura").pack()
estatura = Entry(ventana)
estatura.pack()
def guardar():
    print(esttura.get())
Button(
    ventana,
    text="Guardar",
    command=guardar
).pack()
ventana.mainloop()
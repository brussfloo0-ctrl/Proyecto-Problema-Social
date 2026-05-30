#Fase 1: ventana principal
from tkinter import *
ventana = Tk()
ventana.title("Sistema de Personas Desaparecidas")
ventana.geometry("700x500")
Label(
    ventana,
    text="SISTEMA DE PERSONAS DESAPARECIDAS",
    font=("Arial",16,"bold")
).pack(pady=20)
ventana.mainloop()
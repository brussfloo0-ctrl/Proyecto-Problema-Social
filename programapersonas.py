from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Sistema de Personas Desaparecidas")
ventana.geometry("700x600")
ventana.config(bg="lightblue")

registros = []

Label(
    ventana,
    text="REGISTRO DE PERSONAS DESAPARECIDAS",
    font=("Arial", 16, "bold"),
    bg="lightblue"
).pack(pady=10)

# Nombre
Label(ventana, text="Nombre Completo", bg="lightblue").pack()
nombre = Entry(ventana, width=40)
nombre.pack()

# Edad
Label(ventana, text="Edad", bg="lightblue").pack()
edad = Entry(ventana, width=40)
edad.pack()

# Estatura
Label(ventana, text="Estatura", bg="lightblue").pack()
estatura = Entry(ventana, width=40)
estatura.pack()

# Ojos
Label(ventana, text="Tipo de Ojos", bg="lightblue").pack()
ojos = Entry(ventana, width=40)
ojos.pack()

# Nariz
Label(ventana, text="Tipo de Nariz", bg="lightblue").pack()
nariz = Entry(ventana, width=40)
nariz.pack()

# Boca
Label(ventana, text="Tipo de Boca", bg="lightblue").pack()
boca = Entry(ventana, width=40)
boca.pack()

# Vestimenta
Label(ventana, text="Vestimenta", bg="lightblue").pack()
vestimenta = Entry(ventana, width=40)
vestimenta.pack()

# Lugar
Label(ventana, text="Último Lugar Donde Fue Visto/a", bg="lightblue").pack()
lugar = Entry(ventana, width=40)
lugar.pack()

lista = Listbox(ventana, width=80, height=10)
lista.pack(pady=10)

def registrar():

    datos = {
        "Nombre": nombre.get(),
        "Edad": edad.get(),
        "Estatura": estatura.get(),
        "Ojos": ojos.get(),
        "Nariz": nariz.get(),
        "Boca": boca.get(),
        "Vestimenta": vestimenta.get(),
        "Lugar": lugar.get()
    }

    registros.append(datos)

    texto = (
        f"{datos['Nombre']} | "
        f"{datos['Edad']} años | "
        f"{datos['Lugar']}"
    )

    lista.insert(END, texto)

    messagebox.showinfo(
        "Registro",
        "Persona registrada correctamente"
    )

    nombre.delete(0, END)
    edad.delete(0, END)
    estatura.delete(0, END)
    ojos.delete(0, END)
    nariz.delete(0, END)
    boca.delete(0, END)
    vestimenta.delete(0, END)
    lugar.delete(0, END)

def mostrar_total():

    messagebox.showinfo(
        "Total",
        f"Personas registradas: {len(registros)}"
    )

Button(
    ventana,
    text="Registrar Persona",
    command=registrar,
    bg="green",
    fg="white"
).pack(pady=5)

Button(
    ventana,
    text="Mostrar Total",
    command=mostrar_total,
    bg="blue",
    fg="white"
).pack(pady=5)

ventana.mainloop()
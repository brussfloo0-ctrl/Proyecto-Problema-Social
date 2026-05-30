#Fase 11: Validaciones
if nombre.get() == "":
    messagebox.showerror(
        "Error",
        "Ingrese un nombre"
    )
    return
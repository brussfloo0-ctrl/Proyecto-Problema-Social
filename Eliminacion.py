#Fase 9: Eliminacion
def eliminar():
    seleccion = lista.curselection()
    if seleccion:
        indice = seleccion[0]
        lista.delete(indice)
        del registros[indice]
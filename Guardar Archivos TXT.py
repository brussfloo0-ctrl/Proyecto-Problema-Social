#Fase 10: Guardar Archivo en txt
archivo = open(
    "personas.txt",
    "w"
)
for persona in registros:
    archivo.write(persona)
archivo.close
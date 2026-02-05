# Apertura y lectura de ficheros Python
# Leer todo el contenido como un solo string
with open("archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)

# "r": modo lectura.
# encoding="utf-8": recomendable para evitar problemas con acentos.
# Con with el fichero se cierra solo al salir del bloque.

# Leer línea por línea
# Opción 1: iterar sobre el archivo
with open("archivo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())
# Opción 2: usar readlines()
with open("archivo.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()  # lista de strings
    for linea in lineas:
        print(linea.strip())

# Modos de apertura más comunes
# "r": leer (fichero debe existir). 
# "w": escribir (sobrescribe si existe).
# "a": añadir al final.
# Añade "b" para binario (por ejemplo "rb").
#Programa para contar las palabras en un archibo de texto.
#1.Pedir al usuario la ruta de un archivo de texto. 
#2.Leer el archivo de texto.
#3.Separar en palabras.
#4.Contar número total de palabras.
#5.Mostrar las 10 palabras más frecuentes y su conteo.

#1.Pedir al usuario la ruta de un archivo de texto.
ruta_arch = input("Introduce la ruta del archivo de texto: ")

#2.Leer el archivo de texto.
try: 
    with open(ruta_arch, "r", encoding="utf-8") as archivo:
        contingut = archivo.read()
except FileNotFoundError:
    print("El archivo especificado no existe.")
    exit(1)

#3.Separar en palabras.
import re # Estas dient a Python que necessitaras eines per buscar, comparar i manipulart text utilitzant patrons.
from collections import Counter # Counter es una clase que se encarga de contar las palabras.
palabras=re.findall(r"\w+", contingut.lower()) # \w+ busca una o més lletres, números o guions baixos.
#lower() et passa el contingut a minúscules per evitar diferenciar entre majúscules i minúscules.

#4.Contar número total de palabras.
total_palabras = len(palabras)
print(f"Total palabras: {total_palabras}.") 

#5.Mostrar las 10 palabras más frecuentes y su conteo.
contador_palabras = Counter(palabras) # Counter es una clase que se encarga de contar las palabras.
mas_comunes = contador_palabras.most_common(10)
print("Palabras más frecuentes:")
for palabra, freq in mas_comunes:
    print(f"{palabra}: {freq}")



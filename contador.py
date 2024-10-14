from collections import Counter

# Leer el contenido del archivo de texto
with open('texto.txt', 'r') as archivo:
    texto = archivo.read()

# Filtrar las letras y convertirlas a minúsculas usando una lista por comprensión
letras = [letra.lower() for letra in texto if letra.isalpha()]

# Utilizar Counter para contar las apariciones de cada letra
apariciones = Counter(letras)

# Ordenar las apariciones en orden descendente y convertir a una lista de tuplas
lista_apariciones = apariciones.most_common()

# Imprimir las apariciones de cada letra
for letra, contador in lista_apariciones:
    print(f'{letra}: {contador}')

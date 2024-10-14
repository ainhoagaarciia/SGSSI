import sys

# Comprobar que se hayan pasado exactamente dos argumentos al script
if len(sys.argv) < 3:
    print("Uso correcto: python modificar_texto.py <letra_a_cambiar> <letra_a_reemplazar>")
    sys.exit()

# Asignar los argumentos a variables de manera más clara
letra_a_cambiar, letra_a_reemplazar = sys.argv[1], sys.argv[2]

# Leer el contenido del archivo de texto
with open('texto.txt', 'r') as archivo:
    texto_original = archivo.read()

# Reemplazar las ocurrencias de la letra especificada
texto_modificado = texto_original.replace(letra_a_cambiar, letra_a_reemplazar)

# Guardar el texto modificado nuevamente en el archivo
with open('texto.txt', 'w') as archivo:
    archivo.write(texto_modificado)

print(f'Se ha reemplazado "{letra_a_cambiar}" por "{letra_a_reemplazar}" en el archivo "texto.txt".')


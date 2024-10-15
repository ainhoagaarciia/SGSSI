#!/bin/bash

# Manejo de opciones de línea de comandos
while getopts "d:h:" flag; do
  case $flag in
    d) dir="$OPTARG";;
    h) target_hash="$OPTARG";;
    *) echo "Uso incorrecto del script."
       echo "Uso: $0 -d <directorio> -h <hash_md5>"
       exit 1;;
  esac
done

# Verificar que se hayan proporcionado los argumentos requeridos
if [ -z "$dir" ] || [ -z "$target_hash" ]; then
  echo "Faltan argumentos."
  echo "Uso: $0 -d <directorio> -h <hash_md5>"
  exit 1
fi

# Validar la existencia del directorio
if [ ! -d "$dir" ]; then
  echo "El directorio '$dir' no existe."
  exit 1
fi

# Inicializar una bandera para verificar si se encontró el hash
found=false

# Iterar sobre los archivos del directorio
for file in "$dir"/*; do
    # Calcular el hash MD5 del archivo actual
    current_hash=$(md5sum "$file" | awk '{print $1}')
    
    if [ "$current_hash" == "$target_hash" ]; then
        echo "El hash MD5 $target_hash se encontró en el archivo: $file"
        found=true
        break  # Detener la búsqueda una vez que se encuentra una coincidencia
    fi
done

# Verificar si se encontró el hash
if [ "$found" == "false" ]; then
    echo "El hash MD5 $target_hash no se encontró en ningún archivo del directorio."
fi

#!/bin/bash
# Script para automatizar git add, commit y push

# Agregar todos los archivos al staging
git add .

# Solicitar mensaje de commit
echo "Ingresa tu mensaje de commit:"
read commit_message

# Realizar commit con el mensaje proporcionado
git commit -m "$commit_message"

# Push de los cambios
git push
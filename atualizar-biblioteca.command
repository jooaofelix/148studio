#!/bin/bash
# Copia as artes e mockups da pasta "01 - ESTUDIO 148" do Google Drive para a Biblioteca 148.
# Rode de novo sempre que colocar artes novas no Drive.
cd "$(dirname "$0")" || exit 1
python3 ferramentas/biblioteca.py
echo
read -n 1 -s -r -p "Aperte qualquer tecla para fechar."

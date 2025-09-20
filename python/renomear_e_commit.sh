#!/bin/bash

# Renomear ficheiros conforme solicitaste
mv variaveis.py lab2_variaveis2.py
mv leitura_de_dados.py lab3_leitura_de_dados.py
mv estrutura_de_control.py lab4_estrutura_de_controlo.py
mv funcoes.py lab5_funcoes.py
mv iterativos_loops.py lab6_iterativos_loops.py
mv import.py lab7_import.py

# Adicionar todas as alterações
git add -A

# Fazer commit das renomeações
git commit -m "Renomear ficheiros para convenção labX_nome"

# (Opcional) fazer push para o remoto
# git push origin main

echo "Renomeações e commit realizados com sucesso."

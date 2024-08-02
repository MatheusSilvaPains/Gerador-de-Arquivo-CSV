# -*- coding: utf-8 -*-
"""Gerador de Arquivo CSV - CEAD 2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nkbnSpPjfdxCiDlJT-p1PqLWEHJixblF
"""

import csv
from google.colab import files

# Função para receber a entrada do usuário
def get_user_input(prompt):
    return input(prompt)

# Função para fazer o upload do arquivo txt
def upload_file():
    uploaded = files.upload()
    for filename in uploaded.keys():
        return filename

#  Função principal para gerar o arquivo CSV
def generate_csv():
    # Receber dados do usuário
    disciplina = get_user_input("Digite o código da DISCIPLINA: ")
    ano = get_user_input("Digite o ANO: ")
    periodo = get_user_input("Digite o PERIODO: ")

    # Upload do arquivo txt com as matrículas dos alunos
    print("Faça o upload do arquivo txt com as matrículas dos alunos:")
    filename = upload_file()

    # Ler as matrículas do arquivo txt
    with open(filename, 'r') as file:
        alunos = file.read().splitlines()

    # Nome do arquivo CSV de saída com o código da disciplina
    global output_csv
    output_csv = f'{disciplina}_disciplinas.csv'

    # Escrever os dados no arquivo CSV com separador ponto e vírgula
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        # Escrever a linha de cabeçalho
        writer.writerow(["DISCIPLINA", "ANO", "PERIODO", "ALUNO"])

        # Escrever os dados dos alunos
        for aluno in alunos:
            writer.writerow([disciplina, ano, periodo, aluno])

    print(f"Arquivo {output_csv} gerado com sucesso!")

# Chamar a função principal
generate_csv()

# Fazer o download do arquivo CSV gerado
files.download(output_csv)
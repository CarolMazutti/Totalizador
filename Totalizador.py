import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Cria uma janela oculta
Tk().withdraw()

# Solicita ao usuário que selecione um arquivo CSV
arquivo = askopenfilename(title="Selecione um arquivo CSV", filetypes=[("CSV files", "*.csv")])

# Verifica se um arquivo foi selecionado
if not arquivo:
    print("Nenhum arquivo selecionado.")
else:
    # Lê os dados do arquivo CSV
    df = pd.read_csv(arquivo)

    # Imprime os dados lidos do arquivo
    print("Dados lidos do arquivo:")
    print(df)

    # Imprime as colunas disponíveis
    print("Colunas disponíveis:", df.columns.tolist())

    # Renomeia as colunas, se necessário
    df.columns = ['Nº. ou Código', 'Data', 'Nota Fiscal', 'Descrição Resumida', 'Entrada (Crédito Passível de Apropriação)', 'Saída, Baixa ou Perda (Dedução de Crédito)', 'Saldo Acumulado (Base do Crédito a ser Apropriado)']

    # Imprime os tipos de dados das colunas
    print("Tipos de dados das colunas:")
    print(df.dtypes)

    # Remove linhas onde a coluna 'Data' é NaN ou não é uma data válida
    df = df[pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce').notna()]

    # Converte a coluna 'Data' para o formato de data
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

    # Converte a coluna 'Entrada (Crédito Passível de Apropriação)' para numérico
    df['Entrada (Crédito Passível de Apropriação)'] = pd.to_numeric(df['Entrada (Crédito Passível de Apropriação)'], errors='coerce')

    # Imprime os valores da coluna 'Entrada (Crédito Passível de Apropriação)'
    print("Valores da coluna 'Entrada (Crédito Passível de Apropriação)':")
    print(df['Entrada (Crédito Passível de Apropriação)'])

    # Solicita o mês e o ano ao usuário
    mes = int(input("Digite o mês (1-12): "))
    ano = int(input("Digite o ano (ex: 2021): "))

    # Filtra os dados pelo mês e ano, ignorando os dias
    resultado = df[(df['Data'].dt.month == mes) & (df['Data'].dt.year == ano)]

    # Imprime o resultado após o filtro
    print("Resultado após filtro de mês e ano:")
    print(resultado)

    # Soma os valores da coluna "Entrada"
    soma = resultado['Entrada (Crédito Passível de Apropriação)'].sum()
    print("Soma dos valores da coluna 'Entrada (Crédito Passível de Apropriação)':", soma)

    print("Tipos de dados das colunas:")
    print(df.dtypes)
    print("Valores únicos na coluna 'Data':")
    print(df['Data'].unique())
    print("Primeiras linhas do DataFrame:")
    print(df.head())
    print("Número de linhas válidas após conversão de 'Data':", df['Data'].notna().sum())
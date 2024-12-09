import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Cria uma janela oculta
Tk().withdraw()

# Solicita ao usuário que selecione um arquivo HTML
arquivo = askopenfilename(title="Selecione um arquivo HTML", filetypes=[("HTML files", "*.html")])

# Verifica se um arquivo foi selecionado
if not arquivo:
    print("Nenhum arquivo selecionado.")
else:
    # Lê os dados do arquivo HTML
    dfs = pd.read_html(arquivo)

    # Verifica se alguma tabela foi encontrada
    if not dfs:
        print("Nenhuma tabela encontrada no arquivo HTML.")
    else:
        df = dfs[0]  # Seleciona a primeira tabela

        # Imprime as primeiras linhas do DataFrame para verificar a estrutura
        print(df.head())
        print("Colunas disponíveis:", df.columns.tolist())

        df.columns = ['Nº. ou Código', 'Data', 'Nota Fiscal', 'Descrição Resumida', 'Entrada (Crédito Passível de Apropriação)', 'Saída, Baixa ou Perda (Dedução de Crédito)', 'Saldo Acumulado (Base do Crédito a ser Apropriado)']

        # Remove linhas onde a coluna 'Data' é NaN ou não é uma data válida
        df = df[pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce').notna()]

        # Converte a coluna 'Data' para o formato de data
        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

        # Solicita o mês e o ano ao usuário
        mes = int(input("Digite o mês (1-12): "))
        ano = int(input("Digite o ano (ex: 2021): "))

        # Filtra os dados pelo mês e ano, ignorando os dias
        resultado = df[(df['Data'].dt.month == mes) & (df['Data'].dt.year == ano)]

        # Soma os valores da coluna "Entrada"
        soma = resultado['Entrada (Crédito Passível de Apropriação)'].sum()

        print(f"A soma da coluna 'Entrada' para {mes}/{ano} é: {soma:.2f}")
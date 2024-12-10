import csv
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def ler_arquivo(arquivo):
    with open(arquivo, 'r') as file:
        leitor = csv.reader(file, delimiter=';')
        dados = list(leitor)
        return dados

def ignorar_cabecalho(dados):
    for i, linha in enumerate(dados):
        if len(linha) > 1 and linha[0].isdigit():
            return dados[i:]
    return dados

def perguntar_mes_ano():
    mes = simpledialog.askstring("Entrada de Mês", "Digite o mês (MM):")
    ano = simpledialog.askstring("Entrada de Ano", "Digite o ano (AAAA):")
    return mes, ano

def totalizar_credito(dados, mes, ano):
    total = 0
    for linha in dados:
        if len(linha) > 4:
            data = linha[1].split('/')
            if len(data) == 3:  # Verifica se a data tem 3 partes
                if data[1] == mes and data[2] == ano:
                    total += float(linha[4].replace('.', '').replace(',', '.'))
    return total

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    arquivo = filedialog.askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])
    return arquivo

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    arquivo = selecionar_arquivo()
    if not arquivo:
        messagebox.showinfo("Informação", "Nenhum arquivo selecionado.")
        return

    dados = ler_arquivo(arquivo)
    dados = ignorar_cabecalho(dados)
    mes, ano = perguntar_mes_ano()

    if not mes or not ano:
        messagebox.showwarning("Aviso", "Mês e ano devem ser preenchidos.")
        return

    total = totalizar_credito(dados, mes, ano)
    messagebox.showinfo("Resultado", f"O total de crédito para o mês {mes}/{ano} é: {total:.2f}")

if __name__ == "__main__":
    main()
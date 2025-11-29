import os
from ast import literal_eval

def salvar_arquivo(nome_arquivo, lista_dados):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for d in lista_dados:
            f.write(repr(d) + "\n")


def carregar_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return []

    lista = []
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        for linha in f.readlines():
            linha = linha.strip()
            if linha:
                try:
                    lista.append(literal_eval(linha))
                except (ValueError, SyntaxError):
                    continue
    return lista


def obter_entrada(prompt, tipo=str, pode_ser_vazio=False):
    while True:
        try:
            entrada = input(prompt).strip()

            if not entrada and not pode_ser_vazio:
                print("Este campo é obrigatório. Tente novamente.")
                continue

            if not entrada and pode_ser_vazio:
                return ""

            if tipo == int:
                return int(entrada)
            elif tipo == float:
                return float(entrada)
            else:
                return entrada

        except ValueError:
            print(f"Entrada inválida. Esperado: {tipo.__name__}")

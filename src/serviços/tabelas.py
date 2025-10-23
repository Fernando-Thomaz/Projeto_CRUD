# pega a função "get_connet"
from connection import *

# função para criar o banco
def criar_tabela_usu():
    # tratar codigo
    try:
        # conecta o banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # executa o comando no sql
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS TB_USUARIO(
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) NOT NULL UNIQUE,
            SENHA VARCHAR(256) NOT NULL,
            ADMIN INTERGER
        );
        ''')

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar tabela: {e}')
        input(f"Pressione ENTER para continuar")

# função para criar o banco
def criar_tabela_pro():
    # tratar codigo
    try:
        # conecta o banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # executa o comando no sql
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS TB_PRODUTO(
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(120) NOT NULL UNIQUE,
            PRECO INTERGER NOT NULL,
            QUANTIDADE INTERGER NOT NULL
        );
        ''')

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar tabela: {e}')
        input(f"Pressione ENTER para continuar")
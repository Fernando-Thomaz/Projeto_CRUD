# pega a função "get_connet"
from connection import *

# biblioteca
from passlib.hash import pbkdf2_sha256 as sha256

def cadastrar_produto(nome, preco, quant):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # controlar banco
        cursor = conn.cursor()

        # executa em sql
        cursor.execute('INSERT INTO TB_PRODUTO(NOME, PRECO, QUANTIDADE) VALUES(?, ?, ?)', (nome, preco, quant))

        # commita o banco
        conn.commit()
        print('Produto cadastrado com sucesso!!')
        input('Pressione ENTER para continuar')

    # trata erros
    except Exception as e:
        print(f'Falha ao cadastrar produto: {e}')
        input(f"Pressione ENTER para continuar")


# função para criar usuario
def criar_usuario(nome, email, senha):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # executa codigos na sql
        cursor.execute('INSERT INTO TB_USUARIO(NOME, EMAIL, SENHA) VALUES (?, ?, ?)', (nome, email, senha))

        # commita no banco
        conn.commit()
        print('Usuário cadastrado com sucesso!')
        input(f"Pressione ENTER para continuar")


    # trata erros
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para listar usuarios
def listar_produto():
    # trata erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # executa o codigo no sql
        cursor.execute('SELECT ID, NOME, PRECO, QUANTIDADE FROM TB_PRODUTO')
    
        # salva as coisas selecionadas
        produtos = cursor.fetchall()

        # se tiver usuarios
        if produtos:
            print(f'{30*'-'}Lista de produtos!{30*'-'}')
            print(f"ID | DESCRIÇÂO | PREÇO | QUANTIDADE")

            # mostrar os usuarios
            for u in produtos:
                print(f'| {u}')
            input(f"Pressione ENTER para continuar")

        # se nao tiver usuarios
        else:
            print('Nenhum produto encontrado!')
            input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao listar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função de excluir usuario
def vender_produto(quanti, id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # executa no sql
        quantidade = cursor.execute('SELECT QUANTIDADE FROM TB_PRODUTO WHERE ID = ?', (id))
        quanto = quantidade

        # se nao tiver mais produto
        if quanto >= 0:
            # execute o codgio em sql
            cursor.execute('UPDATE TB_PRODUTO SET QUANTIDADE = ? WHERE ID = ?', (quantidade, id))

        else:
            cursor.execute('DELETE FROM TB_PRODUTO WHERE ID = ?', (id))

        # comita no banco
        conn.commit()
        print(f"Produto vendido com sucesso!")
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao vender produto: {e}')
        input(f"Pressione ENTER para continuar")

# função para editar e atualizar os usuarios
def editar_produto(id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        produto = input(f"Digite o nome do novo produto: ").strip().title()
        preco = float(input(f"Digite o novo preço: ").replace(".",","))
        quantidade = int(input(f"Digite a nova quantidade: "))

        # atualiza as informações
        cursor.execute("UPDATE TB_PRODUTO SET NOME = ?, PRECO = ?, QUANTIDADE = ? WHERE ID = ?", (produto, preco, quantidade, id))

        # salvar no banco
        conn.commit()
        print(f"Produto alterado com sucesso!!")
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao editar produto: {e}')
        input(f"Pressione ENTER para continuar")

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
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(256)
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
            NOME VARCHAR(120) NOT NULL,
            PRECO INTERGER NOT NULL,
            QUANTIDADE INTERGER NOT NULL
        );
        ''')

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar tabela: {e}')
        input(f"Pressione ENTER para continuar")
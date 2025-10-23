# pega a função "get_connet"
from connection import *

# função para deletar produtos
def excluir_produto(id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # atualiza as informações
        cursor.execute("DELETE FROM TB_PRODUTO WHERE ID = ?", (id))

        # salvar no banco
        conn.commit()
        print(f"Produto exlcuido com sucesso!!")
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao editar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função cadastrar produto
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
        cursor.execute('SELECT QUANTIDADE FROM TB_PRODUTO WHERE ID = ?', (id))

        quantidade = cursor.fetchone()
        
        if quantidade[0] < quanti:
            print(f'Não temos essa quantidade no estoque')
            input(f"Pressione ENTER para continuar")

        else:
            quantidade = quantidade[0] - quanti

            cursor.execute('UPDATE TB_PRODUTO SET QUANTIDADE = ? WHERE ID = ? ', (quantidade, id))

            # comita no banco
            conn.commit()
            print(f"Produto vendido com sucesso!")
            input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao vender produto: {e}')
        input(f"Pressione ENTER para continuar")

# função para editar e atualizar os usuarios
def editar_produto(produto, preco, quantidade, id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

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
# pega a função "get_connet"
from connection import *

# biblioteca
from passlib.hash import pbkdf2_sha256 as sha256

# função listar usuario
def listar_info(email):
    # trata erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # executa o codigo no sql
        cursor.execute('SELECT ID, NOME, EMAIL, SENHA, ADMIN FROM TB_USUARIO WHERE EMAIL = ?', (email))
    
        # salva as coisas selecionadas
        produtos = cursor.fetchall()

        if produtos:
            print(f'{30*'-'}Usuario{30*'-'}')
            print(f"ID | NOME | EMAIL | SENHA | ADMIN")

            # mostrar os usuarios
            for u in produtos:
                print(f'| {u}')
            input(f"Pressione ENTER para continuar")

        # se nao tiver usuarios
        else:
            print('Nenhum usuario encontrado!')
            input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao listar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para excluir usuario
def excluir_conta(email):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # atualiza as informações
        cursor.execute("DELETE FROM TB_USUARIO WHERE EMAIL = ?", (email))

        # salvar no banco
        conn.commit()
        print(f"Usuario excluido com sucesso!!")
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao excluir usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para alterar usuario
def troca_senha(senha, email):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # criptografa as senha
        senha = sha256.hash(senha)

        # atualiza as informações
        cursor.execute("UPDATE TB_USUARIO SET SENHA = ? WHERE EMAIL = ?", (senha, email))

        # salvar no banco
        conn.commit()
        print(f"alterado com sucesso!!")
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao editar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para alterar usuario
def troca_email(email, senha):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # atualiza as informações
        cursor.execute("UPDATE TB_USUARIO SET EMAIL = ? WHERE SENHA = ?", (email, senha))

        # salvar no banco
        conn.commit()
        print(f"alterado com sucesso!!")
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao editar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para alterar usuario
def troca_nome(email, nome):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # atualiza as informações
        cursor.execute("UPDATE TB_USUARIO SET NOME = ? WHERE EMAIL = ?", (nome, email))

        # salvar no banco
        conn.commit()
        print(f"alterado com sucesso!!")
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao editar usuario: {e}')
        input(f"Pressione ENTER para continuar")
# pega a função "get_connet"
from connection import *

# biblioteca
from passlib.hash import pbkdf2_sha256 as sha256

# função listar usuario
def listar_usuario():
    # trata erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # executa o codigo no sql
        cursor.execute('SELECT ID, NOME, EMAIL, SENHA, ADMIN FROM TB_USUARIO')
    
        # salva as coisas selecionadas
        produtos = cursor.fetchall()

        # se tiver usuarios
        if produtos:
            print(f'{30*'-'}Lista de usuarios!{30*'-'}')
            print(f"ID | NOME | EMAIL | SENHA | ADMIN")

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

# função para excluir usuario
def excluir_usuario(id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # atualiza as informações
        cursor.execute("DELETE FROM TB_USUARIO WHERE ID = ?", (id))

        # salvar no banco
        conn.commit()
        print(f"Usuario exlcuido com sucesso!!")
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao editar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para alterar usuario
def alterar_usuario(nome, email, senha, admin, id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # criptografa as senha
        senha = sha256.hash(senha)

        # atualiza as informações
        cursor.execute("UPDATE TB_USUARIO SET NOME = ?, EMAIL = ?, SENHA = ?, ADMIN = ? WHERE ID = ?", (nome, email, senha, admin, id))

        # salvar no banco
        conn.commit()
        print(f" alterado com sucesso!!")
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao editar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para criar usuario
def criar_usuario(nome, email, senha):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet_pro()

        # comanda o banco
        cursor = conn.cursor()

        # criptografa
        senha = sha256.hash(senha)

        # executa codigos na sql
        cursor.execute('INSERT INTO TB_USUARIO(NOME, EMAIL, SENHA) VALUES (?, ?, ?)', (nome, email, senha))

        # commita no banco
        conn.commit()
        print('Usuário cadastrado com sucesso!')
        input(f"Pressione ENTER para continuar")
        return True

    # trata erros
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')
        input(f"Pressione ENTER para continuar")
        return False

# função admin
def menu_admin(email, senha):
    try:
        # conectar ao banco
        conn = get_connet_pro()

        # controlar o banco
        cursor = conn.cursor()

        # executa o comando em sql
        cursor.execute('SELECT SENHA, ADMIN FROM TB_USUARIO WHERE EMAIL = ?', (email,))

        # guarda em uma variavel
        result = cursor.fetchone()

        # se tiver algo na variavel
        if result:
            # verifica se a senha esta certa
            if sha256.verify(senha, result[0]) == True:
                print(f'Login feito com sucesso!')
                
                # se o usuario tiver o admin
                if result[1] == 1:
                    print(f'Admin conectado')
                    return True
                return False

        # se nao
        else: 
            print(f'Erro no login')
            return False

    # tratar erros
    except Exception as e:
        print(f'Falha ao logar na conta: {e}')
        input(f"Pressione ENTER para continuar")

# função para logar conta
def logar_usuario(email, senha):
    try:
        # conectar ao banco
        conn = get_connet_pro()

        # controlar o banco
        cursor = conn.cursor()

        # execute o codigo em sql
        cursor.execute('SELECT SENHA FROM TB_USUARIO WHERE EMAIL = ?', (email,))

        # guarda o resultado em uma variavel
        result = cursor.fetchone()
        
        # se tiver algo na variavel
        if result:
            # verifica a senha
            if sha256.verify(senha, result[0]) == True:
                print(f'Login feito com sucesso!')
                return True

        # se nao
        else: 
            print(f'Erro no login')
            return False

    # tratar erros
    except Exception as e:
        print(f'Falha ao logar na conta: {e}')
        input(f"Pressione ENTER para continuar")
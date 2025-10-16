# pega a função "get_connet"
from connection import get_connet

# biblioteca
from passlib.hash import pbkdf2_sha256 as sha256

# função para criar usuario
def criar_usuario(nome, email, senha):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet()

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
def listar_usuario(nome):
    # trata erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

        # executa o codigo no sql
        cursor.execute('SELECT ID, NOME, EMAIL, SENHA FROM TB_USUARIO WHERE NOME = ?',(nome,))
    
        # salva as coisas selecionadas
        usuarios = cursor.fetchall()

        # se tiver usuarios
        if usuarios:
            print(f'{30*'-'}Lista de usuarios!{30*'-'}')

            # mostrar os usuarios
            for u in usuarios:
                print(f'| {u}')
            input(f"Pressione ENTER para continuar")

        # se nao tiver usuarios
        else:
            print('Nenhum usuário encontrado!')
            input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao listar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função de excluir usuario
def excluir_usuario(id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

        # executa o codigo no sql
        cursor.execute("DELETE FROM TB_USUARIO WHERE ID = ?", (id,))
        
        # comita no banco
        conn.commit()
        print(f"Usuario deletado com sucesso!")
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao excluir usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para editar e atualizar os usuarios
def editar_usuario(id, escolha):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

        # possiveis escolhas
        match escolha:
            case "1":
                nome = input(f"Digite seu novo nome: ").strip().title()

                # atualiza as informações
                cursor.execute("UPDATE TB_USUARIO SET NOME = ? WHERE ID = ?", (nome, id))
                print(f"Nome alterado com sucesso!!")

            case "2":
                email = input(f"Digite seu novo email: ").strip().title()

                # atualiza as informações
                cursor.execute("UPDATE TB_USUARIO SET EMAIL = ? WHERE ID = ?", (email, id))
                print(f"Email alterado com sucesso!!")

            case "3":
                senha = input(f"Digite a sua nova senha: ").strip()

                # atualiza as informações
                cursor.execute("UPDATE TB_USUARIO SET SENHA = ? WHERE ID = ?", (senha, id))
                print(f"Senha alterada com sucesso!!")
                

        # salvar no banco
        conn.commit()
        input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao editar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para mostrar os emails dos usuarios
def listar_usuario_email(email):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

        # executa o codigo no sql
        cursor.execute('SELECT ID, NOME, EMAIL, SENHA FROM TB_USUARIO WHERE EMAIL = ?',(email,))
    
        #
        usuarios = cursor.fetchall()

        # se tiver usuarios
        if usuarios:
            print(f'{30*'-'}Lista de usuarios!{30*'-'}')

            # mostrar os usuarios
            for u in usuarios:
                print(f'| {u}')
            input(f"Pressione ENTER para continuar")

        # se nao tiver usuarios
        else:
            print('Nenhum usuário encontrado!')
            input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao listar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para mostrar os ids dos usuarios
def listar_usuario_id(id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

        # executa o codigo no sql
        cursor.execute('SELECT ID, NOME, EMAIL, SENHA FROM TB_USUARIO WHERE ID = ?',(id,))
    
        #
        usuarios = cursor.fetchall()

        # se tiver usuarios
        if usuarios:
            print(f'{30*'-'}Lista de usuarios!{30*'-'}')

            # mostrar os usuarios
            for u in usuarios:
                print(f'| {u}')
            input(f"Pressione ENTER para continuar")

        # se nao tiver usuarios
        else:
            print('Nenhum usuário encontrado!')
            input(f"Pressione ENTER para continuar")

    # tratar erros
    except Exception as e:
        print(f'Falha ao listar usuario: {e}')
        input(f"Pressione ENTER para continuar")

# função para criar o banco
def criar_tabela():
    # tratar codigo
    try:
        # conecta o banco
        conn = get_connet()

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
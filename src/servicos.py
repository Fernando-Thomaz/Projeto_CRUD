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
        cursor.execute('INSERT INTO TB_USUARIO(nome, email, senha) VALUES (?, ?, ?)',
                       (nome, email, senha)
        )

        # commita no banco
        conn.commit()
        print('Usuário cadastrado com sucesso!')

    # trata erros
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

# função para listar usuarios
def listar_usuario():
    # trata erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

        # executa o codigo no sql
        cursor.execute('SELECT NOME, EMAIL, SENHA FROM TB_USUARIO')

        #
        usuarios = cursor.fetchall()

        # se tiver usuarios
        if usuarios:
            print(f'{30*'-'}Lista de usuarios!{30*'-'}')

            # mostrar os usuarios
            for u in usuarios:
                print(f'| {u}')

        # se nao tiver usuarios
        else:
            print('Nenhum usuário encontrado!')

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

# função de excluir usuario
def excluir_usuario(id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

        # executa o codigo no sql
        cursor.execute("""
            DELETE FROM TB_USUARIO WHERE ID=?
        """, (id,))
        
        # comita no banco
        conn.commit()

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

# função para editar e atualizar os usuarios
def editar_usuario(id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

# função para mostrar os emails dos usuarios
def listar_usuario_email(email):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

# função para mostrar os ids dos usuarios
def listar_usuario_id(id):
    # tratar erros
    try:
        # conecta ao banco
        conn = get_connet()

        # comanda o banco
        cursor = conn.cursor()

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar usuario: {e}')

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
        CREATE TABLE TB_USUARIO(
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255)
        );
        ''')

    # tratar erros
    except Exception as e:
        print(f'Falha ao criar tabela: {e}')
from connection import get_connet
from passlib.hash import pbkdf2_sha256 as sha256

def criar_usuario(ID, NOME, EMAIL, SENHA):
    try:
        conn = get_connet()
        cursor = conn.cursor()

        cursor.execute('INSERT INTO TB_USUARIO(ID, NOME, EMAIL, SENHA) VALUES (?, ?, ?, ?)',
                        (ID, NOME, EMAIL, SENHA)
        )

        conn.commit()
        print('Usuário cadastrado com sucesso!')

    except Exception as e:
        print(f'Falha ao criar tabela: {e}')

    finally:
        cursor.close()
        conn.close()

def listar_usuario():
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute("SELECT ID, NOME, EMAIL, SENHA FROM TB_USUARIO")
        usuario = cursor.fetchall
        if usuario:
            print(f"{30*"-"}Lista de usuários!{30*"-"}")
            for u in usuario:
                print(u)
        
        else:
            print("Nenhum usuário encontrado!")

    except Exception as e:
        print(f'Falha ao listar usuario: {e}')

def exlcuir_usuario(ID):
    try:
        conn = get_connet()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM TB_USUARIO WHERE ID = ?
                       ''',(ID))
        conn.commit()
        print(f"Usuário deletado com sucesso!")

    except Exception as e:
        print(f"Falha em excluir usuario {e}")

def editar_usuario(ID):
    ...

def listar_usuario_email(EMAIL):
    ...

def listar_usuario_id(ID):
    ...

def criar_tabela():
    try:    
        conn = get_connet()
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE TB_USUARIO(
	        ID INTERGER PRIMARY KEY ,
            NOME VARCHAR(120) NOT NULL,
            EMAIL VARCHAR(120) UNIQUE,
            SENHA VARCHAR(255)               
                       
        );                            
        ''')

    except Exception as e:
        print(f'Falha ao criar tabela: {e}')
    
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    criar_tabela()
    ID = input('Digite um id: ')
    nome = input('Digite um nome: ').strip().title()
    email = input('Digite o email: ').strip()
    senha = input('Digite uma senha: ').strip()
    senha = sha256.hash(senha)
    print(senha)
    criar_usuario(ID, nome, email, senha)
    listar_usuario()
    exlcuir_usuario(ID)
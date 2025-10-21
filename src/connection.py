# importa banco
import sqlite3

# função para conectar o banco ao back
def get_connet_pro():
    # trata erros
    try:
        # conecta ao banco "controle_usuario.db"
        conexao = sqlite3.connect("controle_produto.db")
        print("Conexão bem sucedida!")
        return conexao
    
    # trata erros
    except sqlite3.Error as e:
        print(f"Falha na conexão {e}")
        return None
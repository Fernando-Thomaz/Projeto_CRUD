# importa as funções do "servicos"
from controles.menu_produto import *
from controles.menu_usuario import *
from serviços.tabelas import *
from serviços.usuario import *
# biblioteca
import os

# limpar tela
limpar = lambda:os.system("cls" if os.name == "nt" else "clear")

# criar tabela se nao tiver
criar_tabela_usu()
criar_tabela_pro()

# função de login e cadastrar
def menu_conta():
    while True:
        try:
            limpar()
            #menu
            print(f"{30*"-"}Conta{30*"-"}")
            print(f"1 - Cadastrar")
            print(f"2 - Login")
            print(f"3 - Admin")
            print(f"4 - Sair")

            # usuario escolhe
            escolha = input(f"Escolha uma opção: ")
            
            # opções
            match escolha:
                case "1":
                    nome = input(f'Digite o nome da conta: ').strip().title()
                    email = input(f'Digite o email da conta: ').strip().title()
                    senha = input(f'Digite a senha da conta: ').strip()
                    if criar_usuario(nome, email, senha) == True:
                        menu_principal()

                case "2":
                    email = input(f'Digite o email da conta: ').strip().title()
                    senha = input(f'Digite a senha da conta: ').strip()
                    if logar_usuario(email, senha) == True:
                        menu_principal()

                case "3":
                    email = input(f'Digite o email da conta: ').strip().title()
                    senha = input(f'Digite a senha da conta: ').strip()
                    if menu_admin(email, senha) == True:
                        menu_admin()

                case "4":
                    print(f'Saindo do sistema...')
                    exit()

        # tratar erros
        except Exception as e:
            print(f"ERROR: {e}")
            input(f"Pressione ENTER para continuar")

# so roda o codigo se a branch for main
if __name__ == '__main__':
    menu_conta()
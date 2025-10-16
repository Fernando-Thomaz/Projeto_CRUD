# importa as funções do "servicos"
from servicos import *

# biblioteca
import os

# limpar tela
limpar = lambda:os.system("cls" if os.name == "nt" else "clear")

# criar tabela se nao tiver
criar_tabela()

# função de menu
def menu():
    # loop
    while True:
        # tratar erros
        try:
            limpar()
            #menu
            print(f"{30*"-"}CONTROLE DE USUARIOS{30*"-"}")
            print(f"1 - Create")
            print(f"2 - Read")
            print(f"3 - Update")
            print(f"4 - Delete")
            print(f"5 - Exit")

            # usuario escolhe
            escolha = input(f"Escolha uma opção: ").strip()

            # escolhas da escolha
            match escolha:
                case "1":
                    # usuario digita
                    nome = input(f"Digite o nome do usuario: ").strip().title()
                    email = input(f"Digite o email do usuario: ").strip().title()
                    senha = input(f"Digite a senha do usuario: ").strip()
                
                    criar_usuario(nome, email, senha)

                case "2":
                    limpar()
                    #menu
                    print(f"{30*"-"}LISTAR{30*"-"}")
                    print(f"1 - Procurar usuario pelo nome")
                    print(f"2 - Procurar usuario pelo email")
                    print(f"3 - Procurar usuario pelo id")

                    # usuario escolhe
                    listar = input(f"Escolha uma opção: ").strip()

                    # escolhas da listar
                    match listar:
                        case "1":
                            nome = input(f"Digite o nome do usuario que quer listar: ").strip().title()
                            listar_usuario(nome)

                        case "2":
                            email = input(f"Digite o email do usuario que quer listar: ").strip().title()
                            listar_usuario_email(email)

                        case "3":
                            # usuario informa
                            id = input(f"Digite o id do usuario que quer listar: ").strip()
                            listar_usuario_id(id)

                case "3":
                    id = input(f"Digite o id do usuario que você deseja editar: ").strip()
                    limpar()
                    # menu
                    print(f"{30*"-"}EDITAR{30*"-"}")
                    print(f"1 - Editar o nome")
                    print(f"2 - Editar o email")
                    print(f"3 - Editar o senha")

                    # usuario escolhe
                    escolha = input(f"Escolha uma opção: ").strip()
                    editar_usuario(id, escolha)

                case "4":
                    id = input(f"Digite o id do usuario que você deseja excluir: ").strip()
                    excluir_usuario(id)

                case "5":
                    print(f"Saindo do sistema...")
                    break

        # tratar erros
        except Exception as e:
            print(f"ERROR: {e}")
            input(f"Pressione ENTER para continuar")

# so roda o codigo se a branch for main
if __name__ == '__main__':
    menu()
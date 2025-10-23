# importa as funções do "servicos"
from serviços.usuario import *
from serviços.produtos import *
from serviços.tabelas import *
from serviços.gerenciamento import *

# biblioteca
import os
import pwinput

# limpar tela
limpar = lambda:os.system("cls" if os.name == "nt" else "clear")

# função de menu do admin
def admin():
    while True:
        try:
            limpar()
            #menu
            print(f"{30*"-"}Admin{30*"-"}")
            print(f"1 - Excluir usuario")
            print(f"2 - Alterar usuario")
            print(f'3 - Listar usuarios')
            print(f'4 - Deletar produtos')
            print(f"5 - Voltar")

            # usuario escolhe
            escolha = input(f"Escolha uma opção: ")
            
            match escolha:
                case "1":
                    # lista usuario
                    listar_usuario()

                    # usurio insere
                    id = input(f'Digite o id do usuario que deseja excluir: ').strip()

                    # chama função
                    excluir_usuario(id)

                case "2":
                    # lista usuario
                    listar_usuario()

                    # usuario insere
                    id = input(f'Digite o id do usuario que deseja alterar').strip()
                    nome = input(f"Digite o nome do usuario: ").strip().title()
                    email = input(f"Digite o novo email: ").strip().title()
                    senha = pwinput.pwinput(prompt="Digite a nova senha: ").strip()
                    admin = int(input(f'Digite o nivel de admin (1, 0): '))

                    # chama função
                    alterar_usuario(nome, email, senha, admin, id)

                case "3":
                    # lista usuario
                    listar_usuario()

                case "4":
                    # lista produto
                    listar_produto()
                    id = input(f'Digite o id do usuario que deseja excluir: ')
                    excluir_produto(id)

                case "5":
                    print(f"Saindo do sistema...")
                    break

        # tratar erros
        except Exception as e:
            print(f"ERROR: {e}")
            input(f"Pressione ENTER para continuar")

# função de gerenciamento de conta
def menu_gerenciamento(email, senha):
    # loop
    while True:
        # tratar erros
        try:
            limpar()
            #menu
            print(f"{30*"-"}Gerenciamento de conta{30*"-"}")
            print(f"1 - Listar informações da conta")
            print(f"2 - Alterar informações da conta")
            print(f"3 - Excluir conta")
            print(f"4 - Voltar")

            # usuario escolhe
            escolha = input(f'Escolha uma opção: ')

            match escolha:
                case "1":
                    listar_info(email)

                case "2":
                    while True:
                        print(f'{30*"-"}Alterar informações da conta{30*"-"}')
                        print(f'1 - Alterar senha da conta')
                        print(f'2 - Alterar email da conta')
                        print(f'3 - Alterar nome da conta')
                        print(f'4 - Voltar')

                        escolha = input(f'Escolha uma opção: ')

                        match escolha:
                            case "1":
                                senha = input(f'Digite a sua nova senha ou pressione ENTER para cancelar: ').strip()
                                if senha != "":
                                    troca_senha(senha, email)

                            case "2":
                                email = input(f'Digite o seu novo email ou pressione ENTER para cancelar: ').strip()
                                if email != "":
                                    troca_email(email, senha)

                            case "3":
                                nome = input(f'Digite o seu novo nome ou pressione ENTER para cancelar: ').strip()
                                if nome != "":
                                    troca_nome(nome, email)

                            case "4":
                                break

                case "3":
                    excluir_conta(email)

                case "4":
                    break

        # tratar erros
        except Exception as e:
            print(f"ERROR: {e}")
            input(f"Pressione ENTER para continuar")
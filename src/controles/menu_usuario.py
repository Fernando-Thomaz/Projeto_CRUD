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
                    id = input(f'Digite o id do usuario que deseja excluir ou pressione ENTER para cancelar: ').strip()

                    if id != "":
                        # chama função
                        excluir_usuario(id)

                case "2":
                    # lista usuario
                    listar_usuario()
                
                    # usuario insere
                    id = input(f'Digite o id do usuario que deseja alterar ou pressione ENTER para cancelar: ').strip()

                    if id != "":
                        email = identificar_usuario(id)

                        while True:
                            print(f'{30*"-"}Alterar informações da conta{30*"-"}')
                            print(f'1 - Alterar senha da conta')
                            print(f'2 - Alterar email da conta')
                            print(f'3 - Alterar nome da conta')
                            print(f'4 - Voltar')

                            escolha = input(f'Escolha uma opção: ')

                            match escolha:
                                case "1":
                                    nova_senha = pwinput.pwinput(prompt='Digite a sua nova senha ou pressione ENTER para cancelar: ').strip()
                                    if nova_senha != "":
                                        troca_senha(nova_senha, email[0])

                                case "2":
                                    novo_email = input(f'Digite o seu novo email ou pressione ENTER para cancelar: ').strip().title()
                                    if novo_email != "":
                                        if troca_email(novo_email, email[0]) == novo_email:
                                            email = novo_email

                                case "3":
                                    novo_nome = input(f'Digite o seu novo nome ou pressione ENTER para cancelar: ').strip().title()
                                    if novo_nome != "":
                                        troca_nome(novo_nome, email[0])

                                case "4":
                                    break

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
def menu_gerenciamento(email):
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
                                nova_senha = pwinput.pwinput(prompt='Digite a sua nova senha ou pressione ENTER para cancelar: ').strip()
                                if nova_senha != "":
                                    troca_senha(nova_senha, email)

                            case "2":
                                novo_email = input(f'Digite o seu novo email ou pressione ENTER para cancelar: ').strip().title()
                                if novo_email != "":
                                    if troca_email(novo_email, email) == novo_email:
                                        email = novo_email

                            case "3":
                                novo_nome = input(f'Digite o seu novo nome ou pressione ENTER para cancelar: ').strip().title()
                                if novo_nome != "":
                                    troca_nome(novo_nome, email)

                            case "4":
                                break

                case "3":
                    excluir_conta(email)
                    break

                case "4":
                    break

        # tratar erros
        except Exception as e:
            print(f"ERROR: {e}")
            input(f"Pressione ENTER para continuar")
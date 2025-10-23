# importa as funções do "servicos"
from serviços.servicos import *
from serviços.produtos import *
from serviços.tabelas import *

# biblioteca
import os
import pwinput

# limpar tela
limpar = lambda:os.system("cls" if os.name == "nt" else "clear")

# criar tabela se nao tiver
criar_tabela_usu()
criar_tabela_pro()

# função de login e cadastrar
def conta():
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
            
            match escolha:
                case "1":
                    # usuario insere
                    nome = input(f'Digite o nome do usuario: ').strip().title()
                    email = input(f'Digite o email do usuario: ').strip().title()
                    senha = pwinput.pwinput(prompt="Digite a nova senha: ").strip()
                    admin = input('dads')

                    # se a função retornar com True
                    if criar_usuario(nome, email, senha, admin) == True:
                        break

                    # se nao
                    else: 
                        pass

                case "2":
                    # usuario insere
                    email = input(f'Digite o email do usuario: ').strip().title()
                    senha = pwinput.pwinput(prompt="Digite a nova senha: ").strip()

                    # se a função retorna com True
                    if logar_usuario(email, senha) == True:
                        break

                    # se nao
                    else:
                        pass

                case "3":
                    # usuario insere
                    email = input(f'Digite o email do usuario: ').strip().title()
                    senha = pwinput.pwinput(prompt="Digite a nova senha: ").strip()

                    # se a função retorna o True
                    if admin(email, senha) == True:
                        # roda função menu
                        menu_admin()

                    # se nao
                    else:
                        print(f'Admin não aceito')
                        pass

                case "4":
                    print(f"Saindo do sistema...")
                    exit()

        # tratar erros
        except Exception as e:
            print(f"ERROR: {e}")
            input(f"Pressione ENTER para continuar")

# função de menu do admin
def menu_admin():
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

# função de menu
def menu_principal():
    # loop
    while True:
        # tratar erros
        try:
            limpar()
            #menu
            print(f"{30*"-"}Mercado{30*"-"}")
            print(f"1 - Cadastrar produto")
            print(f"2 - Listar produtos")
            print(f"3 - Editar produtos")
            print(f"4 - Vender produtos")
            print(f"5 - Sair")

            # usuario escolhe
            escolha = input(f"Escolha uma opção: ").strip()

            # escolhas da escolha
            match escolha:
                case "1":
                    limpar()
                    # usuario digita
                    nome = input(f"Digite o produto que quer adicionar: ").strip().title()
                    preco = float(input(f"Digite o preço do produto: ").strip().replace(".",","))
                    quantidade = int(input(f"Digite a quantidade do preço: ").strip())

                    # chama função
                    cadastrar_produto(nome, preco, quantidade)

                case "2":
                    limpar()
                    
                    # lista produto
                    listar_produto()

                case "3":
                    limpar()

                    # lista produto
                    listar_produto()

                    # usuario digita
                    id = input(f"Digite o id do produto que você deseja editar: ").strip()
                    produto = input(f"Digite o nome do novo produto: ").strip().title()
                    preco = float(input(f"Digite o novo preço: ").replace(".",",").strip())
                    quantidade = int(input(f"Digite a nova quantidade: ").strip())

                    # chama função
                    editar_produto(produto, preco, quantidade, id)

                case "4":
                    limpar()

                    # lista produto
                    listar_produto()

                    # usuario digita
                    id = input(f"Digite o id do produto que você deseja excluir: ").strip()
                    quanti = int(input(f"Digite a quantidade de produto você quer vender: ").strip())

                    # chama função
                    vender_produto(quanti, id)

                case "5":
                    print(f"Saindo do sistema...")
                    break

        # tratar erros
        except Exception as e:
            print(f"ERROR: {e}")
            input(f"Pressione ENTER para continuar")

# so roda o codigo se a branch for main
if __name__ == '__main__':
    conta()
    menu_principal()
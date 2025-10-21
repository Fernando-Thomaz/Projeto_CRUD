# importa as funções do "servicos"
from servicos import *

# biblioteca
import os

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
            print(f"3 - Sair")

            # usuario escolhe
            escolha = input(f"Escolha uma opção: ")
            
            match escolha:
                case "1":
                    ...

                case "2":
                    ...

                case "3":
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
                    # usuario digita
                    nome = input(f"Digite o produto que quer adicionar: ").strip().title()
                    preco = float(input(f"Digite o preço do produto: "))
                    quantidade = int(input(f"Digite a quantidade do preço: "))
                
                    cadastrar_produto(nome, preco, quantidade)

                case "2":
                    limpar()
                    listar_produto()

                case "3":
                    listar_produto()
                    id = input(f"Digite o id do usuario que você deseja editar: ").strip()
                    limpar()
                    editar_produto(id)

                case "4":
                    listar_produto()
                    id = input(f"Digite o id do usuario que você deseja excluir: ").strip()
                    quanti = int(input(f"Digite a quantidade de produto você quer vender: "))
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
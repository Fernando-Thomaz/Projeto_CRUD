# importa as funções do "servicos"
from serviços.usuario import *
from serviços.produtos import *
from serviços.tabelas import *
from controles.menu_usuario import *

# biblioteca
import os

# limpar tela
limpar = lambda:os.system("cls" if os.name == "nt" else "clear")

# função de menu
def menu_principal(email, senha):
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
            print(f'5 - Gerenciamento de conta')
            print(f"6 - Sair")

            # usuario escolhe
            escolha = input(f"Escolha uma opção: ").strip()

            # escolhas da escolha
            match escolha:
                case "1":
                    limpar()
                    # usuario digita
                    nome = input(f"Digite o produto que quer adicionar: ").strip().title()
                    preco = float(input(f"Digite o preço do produto: ").strip().replace(",","."))
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
                    preco = float(input(f"Digite o novo preço: ").replace(",",".").strip())
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
                    menu_gerenciamento(email, senha)

                case "6":
                    print(f"Saindo do sistema...")
                    break

        # tratar erros
        except Exception as e:
            print(f"ERROR: {e}")
            input(f"Pressione ENTER para continuar")
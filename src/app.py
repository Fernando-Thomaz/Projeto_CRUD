def menu():
    while True:
        try:
            print(f"{30*"-"}CONTROLE DE USUARIOS{30*"-"}")
            print(f"1 - Create")
            print(f"2 - Read")
            print(f"3 - Update")
            print(f"4 - Delete")
            print(f"5 - Exit")
            escolha = int(input(f"Escolha uma opção: "))

            match escolha:
                case 1:
                    criar_usuario()

                case 2:
                    print(f"{30*"-"}LISTAR{30*"-"}")
                    print(f"1 - Listar usuario")
                    print(f"2 - Listar email")
                    print(f"3 - Listar id")
                    listar = int(input(f"Escolha uma opção: "))

                    match listar:
                        case 1:
                            listar_usuario()

                        case 2:
                            ...

                        case 3:
                            ...

                case 3:
                    editar_usuario()

                case 4:
                    excluir_usuario()

                case 5:
                    print(f"Saindo do sistema...")
                    exit

        except:
            print(f"Digite um valor valido!")

# so roda o codigo se a branch for main
if __name__ == '__main__':
    menu()
    senha = sha256.hash(senha)
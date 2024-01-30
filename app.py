import os

restaurantes = [
                {'nome': 'Pecorino', 'categoria': 'Italiano', 'ativo': False}, 
                {'nome': 'Hello Kitty Café', 'categoria': 'Cafeteria', 'ativo': True}, 
                {'nome': 'Sukyia', 'categoria': 'Japonesa', 'ativo': False}
                ]

# Função para exibir nome do app
def app_name():
    print("""Sabor Express
        """)

# Função para print do menu
def show_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar estado do Restaurante')
    print('4. Sair')

#Função exit app
def exit_app():
    show_message("Finalizando app")

#função voltar ao menu
def back_menu():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

# Função mostrar mensagem
def show_message(text):
    os.system('cls')
    line = '*' * (len(text))
    print(line)
    print(text)
    print(line)

# Função opção inválida
def invalid_option():
    print("Opção Inválida\n")
    back_menu()

# Função cadastrar
def cadastrar():
    show_message("Cadastro de novos restaurantes\n")

    nome = input("Digite o nome do restaurante que deseja cadastrar: \n")
    cat_res = input(f"Digite a categoria do restaurante {nome}: \n")
    
    dados_res = {'nome': nome, 'categoria': cat_res, 'ativo': False}

    restaurantes.append(dados_res)

    print(f'O restaurante {nome} foi cadastrado com sucesso!')

    back_menu()

# Função Listar restaurante
def listar():
    
    show_message("Restaurantes cadastrados\n")

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status\n')


    for res in restaurantes:
        nome_res = res['nome']
        cat_res = res['categoria']
        active_res = 'Ativado' if res['ativo'] else 'Desativado'
        print(f'- {nome_res.ljust(20)} | {cat_res.ljust(20)} | {active_res}')
    
    back_menu()

# Ativação do restaurante

def alterar_estado_res():
    show_message('Alterando estando do restaurante')

    nome_res = input('Digite o nome do restaurante que deseja alternar o estado: ')
    
    find_res = False

    for res in restaurantes:
        if nome_res == res['nome']:
            find_res = True

            res['ativo'] = not res['ativo']

            msg = f'O restaurante {nome_res} foi ativado com sucesso' if res['ativo'] else f'O restaurante {nome_res} foi desativado com sucesso'
            print(msg)

    if not find_res:
        print('Restaurante não encontrado')

    back_menu()



# Função menu
def menu_options():
    opc_escolhida = int(input('Escolha uma opção: '))

    try:
        if opc_escolhida == 1:
            print('Cadastrar Restaurante')
            cadastrar()
        elif opc_escolhida == 2:
            listar()
        elif opc_escolhida == 3:
            alterar_estado_res()
        elif opc_escolhida == 4:
            exit_app()
        else:
            invalid_option()
    except:
        invalid_option()



def main():
    os.system('cls')
    app_name()
    show_menu()
    menu_options()


if __name__ == '__main__':
    main()

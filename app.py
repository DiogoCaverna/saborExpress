from enum import Enum
import os

restaurantes = ['Pizzaria', 'Peixaria']

def exibir_nome_do_app():
    print('||||||||||Sabor Express||||||||||\n')

def exibir_menu_de_opcoes():
    print('1. Cadastrar Restaurante\n')
    print('2. Listar Restaurante\n')
    print('3. Ativar Restaurante\n')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_menu_principal():
    input('Digite enter para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print('')

def opcao_invalida():
    print('Opcao Invalida\n')
    voltar_menu_principal()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos Restaurantes')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print('')
    print(f'O Restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}\n')

    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar Restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    print('\n')
    exibir_nome_do_app()
    exibir_menu_de_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

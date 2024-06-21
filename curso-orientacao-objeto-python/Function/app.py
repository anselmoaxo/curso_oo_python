import os


restaurantes = restaurantes = [
                                {'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]



def exibir_nome_progrma():
    print('''
        Ｓａｂｏｒ Ｅｘｐｒｅｓｓ 
    ''')

def exibir_opcaoes():
    print('1 - Cadastrar Restaurantes ')
    print('2 - Listar Restaurantes ')
    print('3 - Alternar estado do Restaurantes')
    print('4 - Sair ')
    
def voltar_ao_menu_principal():
    input(' Digite uma tecla para voltar ao Menu incial  ')
    main()
    
def opcao_invalida():
    print('''
          ***Opção Invalida!***
          ''')
    voltar_ao_menu_principal()


def finalizar_app():
    limpar_menu()
    exibir_subtitulo('Encerrando app')


def limpar_menu():
    os.system('clear')

def exibir_subtitulo(texto):
    limpar_menu()
    linha = '=' * (len(texto)+1)
    print(linha)
    print(texto)
    print(linha)
    print()
    

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro Restaurante')
    nome_restaurante = input('Digite o Nome do Restaurante que deseja cadastrar : ')
    categoria = input(f'Digite a Categoria do Restaurante {nome_restaurante} :')
    dados_restaurante = {
        'nome': nome_restaurante,
        'categoria':categoria,
        'ativo': False
    }
    restaurantes.append(dados_restaurante)
    print(f'O Restaurante {nome_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')
    
    print(f'{"Nome do Restaurante".ljust(22)}   {"Categoria".ljust(20)}  {"Status"} ')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome.ljust(20)} - {categoria.ljust(20)} - {ativo} ')
        
    print()
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    
    nome_restaurante = input('Digite o Nome do Restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f' Restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo'] else f' Restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado ')
    
    
    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_selecionada = int(input('Digite a Opção Desejada: '))
        
        if opcao_selecionada == 1:
            cadastrar_novo_restaurante()
        elif opcao_selecionada == 2:
            listar_restaurantes()
        elif opcao_selecionada == 3:
            alternar_estado_restaurante()
        elif opcao_selecionada == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
      
        
def main():
    limpar_menu()
    exibir_nome_progrma()
    exibir_opcaoes()
    escolher_opcao()
        
    
    
    
if __name__ ==  '__main__':
    main()
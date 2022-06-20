import csv
from encodings import utf_8

def cria_arquivo():
    with open('cadastro.csv', 'a') as arquivo:
        cabecalho = csv.writer(arquivo, delimiter=';', lineterminator='\n')
        cabecalho.writerow(['nome', 'email', 'genero', 'instrumento'])


def valida_nome() -> str:
    nome = input('Digite o nome do musico: ').split()
    if ('').join(nome).isalpha():
        return (' ').join(nome).title()
    print('Nome deve conter apenas letras e espaço. Tente novamente..')
    return valida_nome()


def valida_email() -> str:

    with open('cadastro.csv', 'r') as arquivo:
        lista = list(csv.reader(arquivo, delimiter=';', lineterminator='\n'))        

    lista_email = [linha[1] for linha in lista]

    email = input('Digite o e-mail do musico: ').lower().strip()

    if email not in lista_email:
        email_check = email.replace(".", "").replace("_", "").replace("@", "")
        
        if email_check.isalnum() and email.count('@') == 1:
            return email  

        print('E-mail deve conter apenas letras, underscore (_), ponto (.), dígitos numéricos e, obrigatoriamente, exatamente 1 arroba (@)')
        return valida_email()   

    print('E-mail já cadastrado. Tente novamente..')
    return valida_email()


def valida_genero():

    qtd_genero = int(input('Qual a quantidade de genero musical deseja adicionar? '))

    if qtd_genero >= 1:        
        lista_genero = [input(f'Digite o {i+1}° genero  musical do musico: ').title().strip() for i in range(qtd_genero)]   
        return lista_genero      
    
    print('A quantidade de gênero musical deve ser no mínimo 1: ')
    return valida_genero()


def valida_instrumento():

    qtd_instrumento = int(input('Qual a quantidade de instrumento musical deseja adicionar? '))

    if qtd_instrumento >= 1:
        lista_instrumento = [input(f'Digite o {i+1}° instrumento  musical do musico: ').title().strip() for i in range(qtd_instrumento)]
        return lista_instrumento
    
    print('A quantidade de genedo deve ser no mínimo 1: ')
    return valida_instrumento()


def cadastro_musico(nome, email, genero, instrumento):

    with open('cadastro.csv', 'a') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
        escritor.writerow([nome, email, [*genero], [*instrumento]])


def buscar_musicos(nome=None, email=None, genero=None, instrumento=None):
    pass
 
myList = []

def modificar_musicos():
    with open('cadastro.csv', 'r') as file:
        myFile = csv.reader(file)
        for row in myFile:
            myList.append(row)
    print(myList)
    
    print("Por favor veja a lista: ")
    for i in range (len(myList)):
        print("Linha " + str(i) + ": " + str(myList[i]))
    
    editRow = int(input("Qual linha você gostaria de mudar?"))
    
    for i in range(len(myList[0])):
        novosDet = input("Entre novo dado para " + str(myList[0][i] + " :"))
        myList[editRow][i] = novosDet
    
    with open('cadastro.csv', 'w+') as file:
        myFile = csv.writer(file)
        for i in range(len(myList)):
            myFile.writerow(myList[i])
              
def pega_opcao() -> str:
    print("\nDigite a opção desejada: \n",
        "1. Cadastrar músicos\n",
        "2. Buscar músicos\n",
        "3. Modificar músicos\n",
        "4. Montar bandas\n",
        "0. Sair\n"
       )
    return input()

def menu():
    opcoes = {
        "1": cadastro_musico,
        "2": buscar_musicos,
        "3": modificar_musicos
    }

    opcao = pega_opcao()
    
    while opcao != "0":
        if opcao not in opcoes and opcao != "0":
            print("Opção inválida!")
            opcao = pega_opcao()
            continue

        if opcao == '1':
            nome = valida_nome()
            email = valida_email()
            genero = valida_genero()
            instrumento = valida_instrumento() 
            resposta = opcoes[opcao](nome, email, genero, instrumento)
        elif opcao == '2':
            pass
        elif opcao == '3':
            resposta = opcoes[opcao]()
            
        opcao = pega_opcao()
    else:
        print("Obrigado por usar o programa!")  

cria_arquivo()
menu()

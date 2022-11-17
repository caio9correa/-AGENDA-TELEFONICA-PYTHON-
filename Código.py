
import tabulate
agenda = {}

#Essa função busca as chaves de dicionários presentes na agenda.
#Após buscar as chaves a fução vai inserir as chaves dos contatos na lista "Chaves".
def chavescon(agenda, nome):
    chaves = []
    for chave in agenda:
        if chave.startswith(nome):
            chaves.append(chave)
    return chaves


# Esse é o bloco de código responsável por adicionar um contato na agenda.
# Além disso o usuário pode definir a quantidade de contatos que ele pode adicionar e após cadastrar, os dados ficam salvo em um dicionário.
def adicionar():
    Qtdcontatos = int(input('Quantos contatos deseja adicionar? '))
    while Qtdcontatos > 0:
        Nome = input("Digite o nome do contato:")
        Telefone = input("Digite o telefone do contato: ")
        Email = input("Digite o email do contato: ")
        Twitter = input("Digite o Twitter do contato: ")
        Instagram = input("Digite o Instagram do contato: ")
        agenda[Nome] = {
            'Nome': Nome,
            'Telefone': Telefone,
            'Email': Email,
            'Twitter': Twitter,
            'Instagram': Instagram }
        print('O contato {} foi cadastrado com sucesso!'.format(Nome))
        Qtdcontatos = Qtdcontatos - 1

#Esse bloco é o responsável por buscar um contato especifico através do nome na agenda!
#Após buscar os dados do contato, o contado aparece na tela com todos os dados!
def procurarcontato(nome, agenda):
    contatodebusca = []
    chaves1 = chavescon(agenda, nome)
    if len(chaves1) > 0:
        for chave in chaves1:
            contatodebusca.append([
                agenda[chave]["Nome"], agenda[chave]["Telefone"], agenda[chave]["Email"],
                agenda[chave]["Twitter"], agenda[chave]["Instagram"]
            ])
            print(contatodebusca)

#Esse bloco de código é responsável por buscar um contato através do Nome.
#Depois de buscar o contato, ele vai excluir o contato cadastrado.
def apagar(agenda, nome):
    if len(agenda) > 0:
      for contato in list(agenda):
        if contato == nome:
            agenda.pop(nome)
            print("O contato {} foi apagado da agenda!".format(nome))


# Esse bloco de código vai primeiramente buscar o contato cadastrado e os seus dados através do nome.
# Após localizar o contato ele vai pedir para voce inserir os novos dados do contato que deseja alterar.
# Por fim ele vai substituir todos os dados que estavam cadastrados anteriomente!
def Editar(agenda, nome):
    if len(agenda) > 0:
        for chavdocontato in agenda:
            if chavdocontato == nome:
                novo_nome = input('Digite o novo nome do contato: ')
                novo_telefone = input('Digite o novo telefone do contato: ')
                novo_email = input('Digite o novo email do contato: ')
                novo_twitter = input('Digite o novo Twitter do contato: ')
                novo_instagram = input('Informe o novo Instagram do contato: ')
                agenda[novo_nome] = agenda.pop(nome)
                agenda[novo_nome] = {
                    "Nome": novo_nome,
                    "Telefone": novo_telefone,
                    "Email": novo_email,
                    "Twitter": novo_twitter,
                    "Instagram": novo_instagram
                }
                print("Os dados do contato {} foram alterados com sucesso!".format(nome))
                break

#Esse bloco de código é responsável por gerar um relatorio de todos os contatos que estão cadastrados na agenda
#Obs: só consegui gerar o relatorio usando a biblioteca tabulate. Essa biblioteca mostra os contatos em forma de tabela
def relatorio(agenda):
    contatos = []
    if len(agenda) > 0:
        for chave in agenda:
            contatos.append([
                agenda[chave]["Nome"], agenda[chave]["Telefone"], agenda[chave]["Email"], agenda[chave]["Twitter"],
                agenda[chave]["Instagram"]
            ])
        print(tabulate.tabulate(contatos, headers=["Nome", "Telefone", "E-mail", "Twitter", "Instagram"], tablefmt="grid"))
    else:
        print("Agenda vazia!")


# Esse é o menu da minha agenda, onde estão localizadas todas opções.
def menu():
    while True:
        print('--> AGENDA TELEFONICA <--')
        print('1 - Adicionar contato')
        print('2 - Consultar contato')
        print('3 - Excluir contato')
        print('4 - Editar contato')
        print('5 - Lista de contatos')
        print('6 - Sair')
        opc = int(input('Qual a opção desejada: ->'))

        if opc == 1:
            adicionar()
        elif opc == 2:
            nome = input('Digite o Nome que deseja buscar: ')
            procurarcontato(nome, agenda)
        elif opc == 3:
            nome = input('Digite o Nome do contato que deseja excluir: ')
            apagar(agenda, nome)
        elif opc == 4:
            nome = input('Digite o nome do contato que deseja alterar: ')
            Editar(agenda, nome)
        elif opc == 5:
            relatorio(agenda)
        elif opc == 6:
            print('Agenda fechada!')
            break
        else:
            print('Opção invalida, selecione uma opção válida!')
menu()

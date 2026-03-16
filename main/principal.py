from banco.bank import *
from tratamento.erros import *
criar_banco()

def menu(msg):
    for c, s in enumerate(msg, start=1):
        print(f'{c} {s}')



while True:
    menu(['cadastra', 'vizualizar', 'editar', 'deletar'])
    opc = numero(': ')
    if opc >= 5:
        break
    elif opc == 1:
        cadastro = {}
        cadastro['nome'] = input('Nome: ')
        cadastro['email'] = input('email: ')
        cadastro['telefone'] = input('telefone: ')
        cadastro['servicos'] = input('serviços')
        cadastro['preco'] = float(input('preco'))
        cadastro['detalhes'] = input('detalhes')
        adicionar(**cadastro)
    elif opc == 2:
        ver()
    elif opc == 3:
        edite_id = int(input('ID: '))
        edite_nome = input('NOME: ') 
        editar(edite_id, edite_nome)
        
    elif opc == 4:
        delete = int(input('ID: '))
        sn = simounao('tem certeza(sim/nao): ')
        if sn == 'sim':
            excluir(delete)


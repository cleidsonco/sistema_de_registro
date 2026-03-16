def numero(msg):
    while True:
        try:
            numb = int(input(msg))
            
        except ValueError:
            print('digite um numero inteiro')
        else:
            return numb
        


def simounao(r):
    try:
        sina = input(r)
        if sina == 'sim':
            pass
        elif sina == 'nao':
            pass
    except:
        print('escolha uma palavra valida')
    else:
        return sina
    


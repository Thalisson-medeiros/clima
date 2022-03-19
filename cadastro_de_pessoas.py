from func_cadastro import cad_usu, consulta

Lista_cadastro = [[],[],[]]

while True:
    print('[1]Cadastrar Usuários ')
    print('[2]Consultar Usuários ')
    print('[3]Sair ')

    r = input('Opção: ')
    if r not in '1,2,3':
        while True:
            print('Opção incorreta!')
            r = input('Opção: ')
            if r in '1,2,3':
                break

    if r == '1':
        Lista = cad_usu(Lista_cadastro)

    elif r == '2' and Lista_cadastro == [[],[],[]]:
        
        print("-"*100)
        print('{:^100}'.format('Cadastro vazio!'))
        print("-"*100)

    elif r == '2' and Lista_cadastro != []:
        print("-"*100)
        print('[1]Consultar um Único Usuário ')
        print('[2]Consultar Todos os Usuários cadastrados ')

        opc = input('Opção: ')

        if opc == '1':

            consulta(Lista, opc)
        
        elif opc == '2':

            print('-'*100)
            print('{}{: >40}{: >20}'.format('Nome','Idade','E-mail'))
            print('-'*100)

            for c in range(len(Lista[0])):
                
                print('{: <40}{: <18}{}'.format(Lista[0][c],Lista[1][c],Lista[2][c]))
                
            print('-'*100)
    
    else:
        if r == '3':
            break
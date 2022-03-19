def cad_usu(Lista_cadastro):

    print("-"*100)
    print('{:^100}'.format('Cadastro de Usuários'))
    print("-"*100)

    while True:

        Lista_cadastro[0].append(input('Insira o Nome: ').strip())

        Lista_cadastro[1].append(int(input('Insira a Idade: ')))

        email = input('Insira o E-mail: ').strip()
        
        if email not in Lista_cadastro[2]:

            Lista_cadastro[2].append(email)

            print("-"*100)
            print('{:^100}'.format('Usuário cadastrado com Sucesso!'))
            print("-"*100)

        else:  
            while email in Lista_cadastro[2]:

                print("-"*100)
                print('{:^100}'.format('E-mail Já Cadastrado!'))
                print("-"*100)

                novo_email = input('Cadastre outro E-mail : ')

                if novo_email not in Lista_cadastro[2]:

                    Lista_cadastro[2].append(novo_email)
                    break
                    
        print('-'*100)
        p = input('Deseja Cadastrar Um Novo Usuário? [S/N] :').upper()
        print('-'*100)

        if p not in 'N,S':
            while True:
                
                print('Responda Somente [S] Ou [N]')
                
                print('-'*100)
                p = input('Deseja Cadastrar Um Novo Usuário? [S/N] :').upper()
                print('-'*100)

                if p == 'N':
                    return Lista_cadastro
                
                elif p in 'S':
                    break
        
        elif p == 'N':
            return Lista_cadastro



def consulta(Lista,opc):
    if opc == '1':

            validar = input('Insira o e-mail do usuário: ')

            if validar not in Lista[2]:
                
                print("-"*100)
                print('{:^100}'.format('Usuário não encontrado!'))
                print("-"*100)
            
            elif validar in Lista[2]:

               for i in range(len(Lista[2])):
                   
                   if validar == Lista[2][i]:

                       print('-'*100)
                       print('{}{: >40}{: >20}'.format('Nome','Idade','E-mail'))
                       print('-'*100)
                       print('{: <40}{: <18}{}'.format(Lista[0][i],Lista[1][i],Lista[2][i]))
                       print('-'*100)
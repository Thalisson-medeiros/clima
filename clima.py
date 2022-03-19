import requests

API_key = "4177d025896648c1e6f633e45379bd14"

sair = 'off'

while  sair == 'off':

    print('-'*100)
    print('{:^100}'.format('Clima'))
    print('-'*100)

    cidade = input('Informe o nome da cidade: ').lower().strip()
    estado = input('Informe o estado: ').lower().strip()
    pais = "BR"

    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade},{estado},{pais}&appid={API_key}&lang=pt_br"

    try:
        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp']-273.15

    except:
        print('-'*100)
        print('{:^100}'.format('Cidade ou Estado Não Encontrados!'))
        print('-'*100)
        break

    print('-'*100)
    print('{: <20}{: <30}{: <25}'.format('cidade', 'Tempo', 'Temperatura'))
    print('-'*100)
    print('{: <20}{: <30}{:.2f}°C'.format(cidade, descricao, temperatura))
    print('-'*100)

    continuar = input('Quer Buscar outra previsão? [S/N]: ').lower()
    
    if continuar == 'n':
        break

    elif continuar not in 's,n':

        while True:
            print('Resposta inválida!')
            
            resp = input('Digite Somente [S] ou [N]: ')

            if resp == 's':
                break

            else:
                if resp == 'n':
                    sair = 'on'
                    break

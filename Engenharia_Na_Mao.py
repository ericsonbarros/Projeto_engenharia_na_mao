# Modulos importados
from comandos import uteis

# Lista dos serviços oferecidos
serviços = ('revestimento ceramico', 'Pintura', 'Sair')
ceramico = ('revestimento Piso', 'revestimento parede', 'Voltar')

# Layout inicial
print(uteis.linha())
print('  Seja bem vindo(a) a Engenharia na mão')
uteis.cabeçalho('MENU PRINCIPAL')
print(f'{"cod":>5}{"serviços":>30}')
print(uteis.linha())

# Lista dos serviços organizado por codigo
for c,s in enumerate(serviços):
    print(f'{c+1:>5}{s:>30}')
print(uteis.linha())
opc = str(input('Digite o codigo do serviço que deseja acessar: '))

# Seleção de serviço desejado
while opc not in '123':
    print('\033[31mERRO! Digite um codigo valido.\033[m')
    opc = str(input('Digite o codigo do serviço que deseja acessar: '))

# Opção 1 -Revestimento ceramico
if opc == '1':
    uteis.cabeçalho('Calculadora de Revestimento')
    print(f'{"cod":>5}{"serviços":>30}')
    print(uteis.linha())

    # Seleção da calculadora para piso e parede
    for c,s in enumerate(ceramico):
        print(f'{c+1:>5}{s:>30}')
    print(uteis.linha())
    opc = str(input('Digite o codigo do serviço que deseja acessar:'))
    while opc not in '12':
        print('\033[31mERRO! Digite um codigo valido.\033[m')
        opc = str(input('Digite o codigo do serviço que deseja acessar: '))

    # Opção 1 - Revestimento ceramico - piso
    if opc == '1':
        uteis.cabeçalho('Revestimento Piso')

        # Opçao se o Usuario tiver a área do piso
        opc_1 = str(input('Possui a area do piso?[SIM/NAO] ')).strip().upper()[0]
        while opc_1 not in 'SN':
            print('\033[31mERRO! Digite um codigo valido.\033[m')
            opc_1 = str(input('Possui a area do piso?[SIM/NAO] ')).strip().upper()[0]
        # Usuario POSSUI A ÁREA
        if opc_1 == 'S':
            resp_area = float(input('Digite a area do piso(m²): '))
            print(uteis.linha())

            # Verificação se o usuario possui rendimento do material utilizado
            resp_ceramico = str(input('Possui o rendimento do material por caixa?[SIM/NAO]: ')).strip().upper()[0]
            while resp_ceramico not in 'SN':
                print('\033[31mERRO! Digite um codigo valido.\033[m')
                resp_ceramico = str(input('Possui o rendimento do material por caixa?[SIM/NAO]: ')).strip().upper()[0]
                # Usuario POSSUI O RENDIMENTO
            if resp_ceramico == 'S':
                resp_area_ceramico = float(input('Digite o rendimento por caixa(m²): '))
                print(uteis.linha())

                # Calculo de quantidade de porcelanato
                print(f'Se a área do piso possui {resp_area}m² e o rendimento do material é {resp_area_ceramico}\n'
                      f'sera necesasrio {uteis.piso(resp_area, resp_area_ceramico)} caixa para resvestir toda a área desejavel')


    # Opção 2 - Revestimento ceramico - Parede
    if opc == '2':
        uteis.cabeçalho('Revestimento Parede')


#Opção 2 - Pintura
if opc == '2':
    print('pintura')





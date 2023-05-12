from time import sleep
saldo = 5000
saque = []
deposito = []
while True:
    print('{:^40}'.format('*BANCO TABAJARA*'))
    print('''[1] - Saque
[2] - Extrato
[3] - Deposito
[4] - Sair''')
    print()
    operação = int(input('Digite o numero da operação que deseja realiza: '))
    if operação == 1:
        saque.append(int(input('Digite o valor do saque: ')))
        print(f'Saque de R${saque[-1]} realizado com sucesso.')
        saldo = saldo - saque[-1]
    elif operação == 2:
        print('-' *40)
        print('{:^40}'.format("GERANDO EXTRATO"))
        sleep(2)
        print(f'Seu saldo atual é de R${saldo}')
        for v in saque:
            print(f'Saque realizado no valor de R${v}')
        for v in deposito:
            print(f'Deposito realizado no valor de R${v}')
        print('-' *40)
    elif operação == 3:
        deposito.append(int(input('Digite o valor de deposito: ')))
        print(f'Deposito de R${deposito[-1]} realizado com sucesso')
        saldo = saldo + deposito[-1]
        print('-' *40)
    elif operação == 4:
        print('SAINDO...')
        break
print('Obrigado por usar nossos sistemas')
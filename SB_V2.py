from datetime import datetime as dt


menu = """
 [1] |Saque|
 [2] |Deposito|
 [3] |Extrato|
 [0] |Sair|
"""
#variaveis
saldo = 0
extrato = "" 
LIMITE_DE_SAQUE = 500
LIMITE_SAQUE_DIARIO = 10
saques_feitos_hoje = 0
saques_restantes_hoje = 10
agora = dt.now()


#estrutura de repetição
while True:
    opcao = input(menu)
    if not opcao.isdigit():#verifica se não é um numero
        print('Opção invalida, digite apenas numeros.')
        continue #caso não seja, ele retorna ao menu

    if opcao == "1":
        #Selecionando Saque
        while True:
            try:
                valor = float(input('Digite um valor a ser sacado: '))
            except ValueError:
                print('Erro. Digite um numero')
                continue #caso não seja numero, retorna ao valor a ser sacado

            if saldo < valor:
                print('Saldo insuficiente.') #se valor menor que saldo, então a mensagem é exibida

            elif valor > LIMITE_DE_SAQUE:
                print(f'Erro. Limite de saque de {LIMITE_DE_SAQUE:.2f} atingido') # se valor maior que o limite de saque, a mensagem é exibida

            elif saques_feitos_hoje >= LIMITE_SAQUE_DIARIO: #se "saques_feitos_hoje" for igual que o limite de saque, a transação é cancelada
                print('Limite de saque diario atingido.')

            elif valor <= saldo:
                saldo -= valor #subtrai o saldo do valor que será sacado
                print(f'Valor de R${valor}, sacado com sucesso !') #exibe o valor sacado
                extrato += (f"{dt.now().strftime('%d/%m/%Y - %H:%M:%S')} |Saque R${valor:.2f}\n") #:.2f coloca em exibição somente 2 casas decimais
                saques_feitos_hoje += 1 #adiciona o valor de 1 para o saque diario
                saques_restantes_hoje -=1 #diminui em 1 os saques restantes
            break
        else:
            print('Erro. Valor invalido para saque.')
    
    elif opcao == "2":
        #Selecionando Deposito
        while True:
            try:
                valor = float(input("Digite o Valor que deseja depositar: "))
            except ValueError:
                print('Erro. Digite um Numero')
                continue

            if valor > 0: #se valor maior que 0, então o deposito sera realizado
                saldo += valor
                extrato += (f"{dt.now().strftime('%d/%m/%Y - %H:%M:%S')}| Deposito: R${valor:.2f}\n")#adiciona duas casas decimais e diz quando foi feita a transação.
                print('valor depositado.')
                break#fim da repetição

            else:
                print("numero invalido. Erro.")
            
    elif opcao == "3":
        #Selecionando Extrato
        print('======Extrato======')
        if extrato:
            print(extrato)

        else:
            print('Não foram feitas transações para essa conta.')
        #os "prints" alinhados com o if e else estão fora do bloco, logo, não fazem parte da execução. Sempre serão exibidos independente do resultado do if/else.
        print(f'\nsaldo atual de R${saldo:.2f}.')
        print(f'Saques restantes hoje: {saques_restantes_hoje}')
        print('====================')

    
    elif opcao == "0":
        #Sair do programa
        print('fim da execução do programa.')
        break         #termina a execução do programa

    else:
        print('Operação não realizada.')
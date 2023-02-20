from datetime import date
LIMITE_SAQUES = 3
saldo = 2000
contador_saques = 0
lista_saques = [0,0,0]
lista_saldos = [0,0,0]
data_antiga = 0
extrato =''
while(1):
    print("Bem vindo ao banco do Guilherme! Escolha uma opção:\n[1] Sacar\n[2] Consultar Saldo\n[3] Sair")
    opcao=input()
    data_hoje = date.today()
    if (data_antiga == 0):
         data_antiga = date.today()
    if (data_hoje != data_antiga):
        contador_saques = 0
    if (opcao == "1"):
        print("Digite a quantia que você quer sacar ou digite x se você quer retornar ao menu inicial")
        saque = input()
        if(saque[0].isnumeric() and float(saque) > 0 and float(saque) <= 500 and contador_saques<=2):
            #print("Tudo certo!")
            if (float(saldo) < float(saque)):
                print(f"Você não tem saldo suficiente para essa transação! Seu saldo é {saldo}")
            else:
                lista_saldos[contador_saques] = saldo
                saldo-=float(saque)
                lista_saques[contador_saques] = float(saque)
                contador_saques+=1
                data_antiga = date.today()
                print(f"Saque de R$ {saque} realizado com sucesso! Seu novo saldo: {saldo:.2f}")
                extrato += f"Saque: R$ {float(saque):.2f}\n"
        elif (contador_saques>2):
            print("Você ultrapassou o limite de 3 saques diários. Volte amanhã!")
        elif (saque.isnumeric() and float(saque) > 500):
            print("Você está solicitando um saque maior do que seu limite de R$500.00", end="\n")
    if (opcao == "2"):
        print("Segue seu extrato:")
        if(lista_saques[0] != 0):
            print(f"- Saque de {lista_saques[0]}. O saldo anterior a este era de {lista_saldos[0]:.2f}")
        if(lista_saques[1] != 0):
            print(f"- Saque de {lista_saques[1]}. O saldo anterior a este era de {lista_saldos[1]:.2f}")
        if(lista_saques[2] != 0):
            print(f"- Saque de {lista_saques[2]}. O saldo anterior a este era de {lista_saldos[2]:.2f}")
        print({extrato})
        print(f"O saldo atual é de: {saldo:.2f}")
    elif (opcao == "3"):
        print("Obrigado pela preferência!")
        break           
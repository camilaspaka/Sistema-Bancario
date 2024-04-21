#apenas 3 saques diarios
#limite maximo de 500 por saque
#Caso não tenha saldo, deve exibir mensagem de erro
#Todas as operações tem que estar disponiveis no Extrato 
#O formato deve ser R$xxx.xx 
#operação de extrato deve listar todos os depositos e saques realizados

menu = """

  [E]Extrato
  [D]Deposito
  [I]Emprestimo
  [S]Saque
  [Q]Sair

  => """

print(menu)

saldo = 0
limite = 500
extrato = ""
emprestimo = 5000
numero_saques = 0
Limite_Saques = 3

while True:

    opcao = input(menu)

    if opcao == "E":
        print("\n=========================Extrato==============================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")
        print("________________________________________________________________")

    elif opcao == "D":
        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito : R$ {valor:.2f}\n"
        else:
            print("Operação falhou!")

    elif opcao == "I":
        valor = float(input("Qual o valor do emprestimo que deseja realizar?: "))
        if valor > 5000:
            print("Operação falhou! Valor acima do permitido para emprestimo nessa conta!")
        else:    
            print("Emprestimo de R$ {valor:.2f} realizado com sucesso!!!")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= Limite_Saques

        if excedeu_saldo:
            print("Operação não realizada. Realize um emprestimo ou deposite mais dinheiro na conta.") 
        if excedeu_limite:
            print("Operação falhou! Você excedeu o limite diario.")
        if excedeu_saques: 
            print("Operação falhou! Você não pode mais realizar nenhum saque hoje")


    elif opcao == "Q":
        break

 
    else:
        print("Operação invalida, por favor selecione uma opção valida")
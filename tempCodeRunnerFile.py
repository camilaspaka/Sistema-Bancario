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
        print("Extrato")
    elif opcao == "D":
        print("Deposito")
    elif opcao == "I":
        print("Emprestimo")
    elif opcao == "S":
        print("Saque")
    elif opcao == "Q":
        break


    else:
        print("Operação invalida, por favor selecione uma opção valida")
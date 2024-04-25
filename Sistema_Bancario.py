import textwrap

def menu():
    menu = """
    ==============Menu============
    [D]\tDeposito
    [S]\tSaque
    [E]\tExtrato
    [I]\tNova Conta
    [L]\tListar Contas
    [N]\tNovo Usuario
    [Q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("\n===Deposito realizado com sucesso!===")
    else:
        print("\n@@@ Operação falhou! @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
          print("\n@@@ Operação falhou! Sem saldo suficiente! @@@")

    elif excedeu_limite:
          print("\n @@@ Operação falhou! O valor do saque é superior ao valor em conta @@@") 

    elif excedeu_saques:
          print("\n@@@ Operação falhou! Numero maximo de saques permito excedido! @@@")

    elif valor >0:
        saldo -= valor 
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é invalido!!!") 
    
def exibir_extrato(saldo, /, *, extrato):
       print("\n==============Extrato==================")
       print("Não foram realizadas movimentações."if not extrato else extrato)
       print(f"\nSaldo:\t\tR$ {saldo:.2f}")
       print("==========================================")

def criar_usuario(usuarios):
       cpf = input("Informe o CPF: ")
       usuario = filtrar_usuario(cpf, usuarios)

       if usuario:
              print("\n@@@ CPF já cadastrado")
              return
       nome = input("Informe o nome completo: ")
       data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ")
       endereco = input("Informe o endereço(logadouro, nro, bairro, cidade/estado): ")

       usuarios.append({"nome":nome, "data_nascimento": data_nascimento,"cpf":cpf, "endereco":endereco})

       print("=== Usuario cadastrado com sucesso!!! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usario in urusarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
       cpf = input("Informe o CPF do usuario: ")
       usuario = filtrar_usuario(cpf, usuarios)

       if usuarios:
              print("\n=== Conta Criada com Sucesso!!! ===")
              return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

       print("\n@@@ Usuario não localizado! @@@")

def listar_contas(contas):
       for conta in contas:
              linha = f"""\
                    Agencia:\t{conta['agencia']}
                    C/C:\t\t{conta['numero_conta']}
                    Titular:\t{conta['usuario']['nome']}
"""   
              print("=" * 100)
              print(textwrap.dedent(linha))

def main():
       Limite_Saques = 3
       Agencia = "0001"

       saldo = 0
       limite = 500
       extrato = ""
       numero_saques = 0
       usuarios = []
       contas = []

       while True:
            opcao = menu()

            if opcao == "D":
                     valor = float(input("Informe o valor do deposito: "))

                     saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == "S":
                     valor = float(input("Informe o valor do saque: "))

                     saldo, extrato = sacar(
                            saldo = saldo,
                            valor = valor,
                            extrato = extrato,
                            limite = limite,
                            numero_saques= numero_saques,
                            limite_saques= Limite_Saques,
                     )
            elif opcao == "E":
                  exibir_extrato(saldo, extrato=extrato)
       
            elif opcao == "N":
              criar_usuario(usuarios)

            elif opcao == "I":
              numero_conta = len(contas) + 1
              conta = criar_conta(Agencia, numero_conta, usuarios)

            if conta:
                contas.apped(conta)
            
            elif opcao == "L":
              listar_contas(contas)

            elif opcao == "Q":
              break
             
            else:
              print("Operação falhou, tente novamente")

main()
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
            extrato += f"Deposito : R$ {valor:.2f}\n"
            print("\n===Deposito realizado com sucesso!===")
        else:
            print("\n@@@ Operação falhou! @@@")
        return saldo, extrato

   

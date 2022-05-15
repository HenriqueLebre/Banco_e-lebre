from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []


def menu() -> None:
    print('-----------------------------------------------')
    print('------------------ Bem vindo ------------------')
    print('--------------------- ATM ---------------------')
    print('------------------- e-Lebre -------------------')
    print('-----------------------------------------------')

    print('Faça sua choices: ')
    print('1 - Seja um e-lebrer e crie sua conta')
    print('2 - Saque suas criptolebre')
    print('3 - Depositar suas criptolebre')
    print('4 - Transferir suas criptolebre')
    print('5 - Listar as contas Lebres')
    print('6 - Sair do ATM e-lebre')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetua_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('cole sempre que precisar! xD')
        sleep(3)
        exit(0)
    else:
        print('essa opção num existe parsa, meça sua opção ai, pufavo!')
        sleep(3)
        menu()


def criar_conta() -> None:
    print('Fala teus dados ai: ')
    nome: str = input('Nome e-lebrer: ')
    email: str = input('fala teu e-mail p mandar uns trojan: ')
    cpf: str = input('Digite seu CPF: ')
    data_nascimento: str = input('Qual a bonita(o) nasceu, hein: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Parabéns, meu chapa! Sua conta foi criada com sucesso!')
    print(conta)

    sleep(2)
    menu()


def efetua_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Digite sua conta ai parsa: '))

        conta: Conta = busca_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Quanto cê quer sacar: '))

            conta.sacar(valor)
        else:
            print(f'Num existe essa conta aqui {numero}')
    else:
        print('Ainda não temos a quantidade de contas suficientes cadastradas.')
    sleep(3)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Me informa sua conta: '))

        conta: Conta = busca_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do deposito: '))

            conta.depositar(valor)
        else:
            print(f"num achei essa conta ai {numero} não parsa")
    else:
        print('Ainda não temos a quantidade de contas suficientes cadastradas.')
        sleep(2)
        menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_orgin: int = int('Informe o núemero da sua conta')

        conta_orin: Conta = busca_conta_por_numero(numero_orgin)

        if conta_orin:
            numero_destin: int = int(input('Me fala a conta que você que transferir: '))

            conta_dest: Conta = busca_conta_por_numero(numero_destin)

            if conta_orin:
                valor: float = float(input('Informe o valor que você quer enviar: '))

                conta_orin.transferencia(conta_dest, valor)
            else:
                print(f'A conta que você quer transferir nem existe, checa isso ai {numero_destin}!')
        else:
            print(f'cê tá tentando me passar uma conta {conta_orin}que nem existe, toma vergonha')
    else:
        print('Ainda não temos a quantidade de contas suficientes cadastradas.')
        sleep(2)
        menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Lista de contas sobre nossa posse: ')

        for conta in contas:
            print(conta)
            print('xxxxxxxxxxxxxxxxx')
            sleep(1)
    else:
        print('Ainda não temos a quantidade de contas suficientes cadastradas.')
        sleep(2)
        menu()


def busca_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    menu()
# Imports
from models.cliente import Cliente
from utils.helper import float_str_moeda


class Conta:  # Criando a classe Conta do usuário

    codigo: int = 101  # código inicial de contas o "marco zero das contas"

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 10.0
        self.__saldo_total: float = self._calculo_saldo_total
        Conta.codigo += 1

    def __str__(self: object) -> str:  # Definindo o retorno quando cliente solicitar o número da conta e o seu saldo.
        return f'Número da conta: {self.numero} \n' \
               f'Cliente: {self.cliente.nome} \n' \
               f'Saldo Total: {float_str_moeda(self.saldo_total)}'


    @property
    def saldo(self: object) -> float:  # Definindo uma propriedade para o saldo do cliente, retornar o seu saldo
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:  # Setando a property.
        self.__saldo = valor

    @property
    def numero(self: object) -> int:  # Defnindo uma propriedade para o número da conta.
        return self.__numero

    @property
    def saldo_total(self: object) -> float:  # Defnindo uma propriedade para o número da conta.
        return self.__saldo_total

    @property
    def cliente(self: object) -> Cliente:  # Definindo o cliente como o nome.
        return self.__cliente

    @property
    def limite(self: object) -> float:  # Definindo o limite do cliente
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:  # Settando a property
        self.__limite = valor


    @property
    def _calculo_saldo_total(self: object) -> float:  # Definindo o cálculo do saldo total do cliente: saldo + limite
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        pass

    def sacar(self: object, valor: float) -> None:
        pass

    def transferencia(self: object, destino: object, valor: float) -> None:
        pass


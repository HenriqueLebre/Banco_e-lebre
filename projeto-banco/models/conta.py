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

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

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

    def depositar(self: object, valor: float) -> None:  # Definição da lógica em deposito
        if valor > 0:  # Se o valor for maior que zero, ele segue com o processo de deposito
            self.saldo = self.saldo + valor  # Retorna o saldo atual que o usuário tinha + o valor do deposito
            self.saldo_total = self._calculo_saldo_total  # retorna o novo saldo total
            print(f'Parabéns você efetuou um deposito de {valor} lebrers.')
        else:
            print('cê num pode fazer deposito zerado, né parsa.')

    def sacar(self: object, valor: float) -> None:  # Definição da lógica em saque
        if 0 < valor <= self.saldo_total:  # Se o valor for maior que zero e maior ou igual o valor do saldo atual prossegue
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calculo_saldo_total
            else:
                resto: float = self.saldo - valor
                self.limite = self.limite + resto
                self.saldo = 0
                self.saldo_total = self._calculo_saldo_total
                print(f'Parabéns! Você sacou {valor} Lebrers!')

        else:
            print('Num deu certo seu saque :(')

    def transferencia(self: object, destino: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calculo_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calculo_saldo_total
            else:
                resto: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + resto
                self.saldo_total = self._calculo_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calculo_saldo_total
            print(f'Sua transferência de {valor} foi realizada com sucesso, meu chapa!')
        else:
            print(f'Sua transferência de {valor} não foi realizada! Tenta mais tarde, truta!')


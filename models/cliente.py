# Imports
from datetime import date
from utils.helper import data_para_string, str_para_data


class Cliente:  # Criando uma classe de cliente, onde 1001 é o marco zero.
    contador: int = 1001

    def __init__(self: object, nome: str, cpf: str, data_nascimento: str, email: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_para_data(data_nascimento)
        self.__email: str = email
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self: object) -> int:  # Definido o código do cliente.
        return self.__codigo

    @property
    def nome(self:object) -> str:  # Definindo o input que recebe o nome do cliente.
        return self.__nome

    @property
    def email(self: object) -> str:
        return self.__email  # Definido o input que recebe o e-mail do usuario.

    @property
    def cpf(self: object) -> str:  # Definindo o input que recebe o cpf do usuário.
        return self.__cpf

    @property
    def data_nascimento(self: object) -> str:  # Definindo o input que recebe a data de nascimento do cliente.
        return data_para_string(self.__data_nascimento)

    @property
    def data_cadastro(self: object) -> str:  # Definindo a data do cadastro do usuario.
        return data_para_string(self.__data_cadastro)

    def __str__(self: object) -> str:  # Definindo o retorno dos dados do cliente.
        return f'Código: {self.codigo} \nNome: {self.nome} ' \
               f'\nData de Nascimento: {self.data_nascimento} ' \
               f'\nCadastrado em: {self.data_cadastro}'





# Imports
from datetime import date
from datetime import datetime


def data_para_string(data: date) -> str:  # definindo o calculo da data para string.
    return data.strftime('%d/%m/%Y')


def str_para_data(data: str) -> date:  # definindo o calculo da string para date.
    return datetime.strptime(data, '%d/%m/%Y')


def float_str_moeda(valor: float) -> str:  # Ajuste do valor contábil que será usado para calculo, com duas casas décimais.
    return f'R$ {valor:,.2f}'




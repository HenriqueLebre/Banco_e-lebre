from models.cliente import Cliente
from models.conta import Conta


carlin: Cliente = Cliente('Carlin', '351351351', '20/05/2020', 'fsdoaf@dsfuohsdf')

robertin: Cliente = Cliente('robertin', '123465789', '15/07/1997', 'ascds@opçlo')


contaf: Conta = Conta(robertin)

print(contaf)

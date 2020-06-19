
class ContaCorrente:

    def __init__(self, numero, titular, saldo, limite = 1000.0): # definindo limite padrao de 1000.0
        print(f'Construindo Objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print(f'({self.__titular}): Saldo R${self.__saldo}.' )

    def deposito(self, valor):
        self.__saldo += valor
        print(f'({self.__titular}): Depositando {valor}, seu saldo atual é {self.__saldo} ')
    
    def saque(self, valor):
        self.__saldo -= valor
        print(f'({self.__titular}): Saque de R${valor} realizado, seu saldo atual é {self.__saldo}.')

    def transfere(self, valor, destino):
        valor = valor
        self.saque(valor)
        print()
        destino.deposito(valor)
        print()
        self.extrato()

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
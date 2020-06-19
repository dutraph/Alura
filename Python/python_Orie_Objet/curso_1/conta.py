
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
    

    def __pode_sacar(self, valor_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_sacar <= valor_disponivel

    def saque(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f'({self.__titular}): Saque de R${valor} realizado, seu saldo atual é {self.__saldo}.')
        else:
            print(f'Operaçã invalida! o valor de {valor} ultrapassa limite permitido.')
        

    def transfere(self, valor, destino):
        valor = valor
        self.saque(valor)
        print()
        destino.deposito(valor)
        print()
        self.extrato()

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()
    @titular.setter
    def titular(self, nome):
        self.__titular = nome

    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}
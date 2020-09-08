
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo Objeto....{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #self.__codigo_banco = "001"
    def extrato(self):
        print(f"Seu extrato é: R${self.__saldo}")

    def deposita(self, valor):
        self.__saldo+=valor

    def saca(self, valor):
        if valor > (self.__saldo + self.__limite):
            print("Saldo insuficiente")
        else:
            self.__saldo-=valor

    def transfere(self, valor, conta_destino):
        if valor > (self.__saldo + self.__limite):
            print("Saldo insificiente.")
        else:
            self.saca(valor)
            conta_destino.deposita(valor)
            print(f"Valor transferido R${valor}")
    
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return "001"
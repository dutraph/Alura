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
        if  (self.__pode_sacar(valor)):
            self.__saldo-=valor
        else:    
            print("Saldo insuficiente")

    def transfere(self, valor, conta_destino):
            self.saca(valor)
            conta_destino.deposita(valor)
            print(f"Valor transferido R${valor}")
    
    @property #usado como getter e nao preciso de parenteses EX: conta.titular e nao conta.titular() 
    def titular(self):
        return self.__titular
    
    @titular.setter #tambem nao precisa usar parenteses na criaçao de um titual EX: conta.titular = 'paulo' e nao  conta.titular('paulo') 
    def titular(self, titular):
        self.__titular = titular

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
        bancos = {'bradesco': '001', 'Itau': '002', 'caixa': '003'}  # Acesso é feito da seguinte forma: <Class name>.codigo_banco(), podemos add numa vaiavel e acessar os valores individuais: bancos = Conta.codigo_banco(), bancos['']
        return bancos

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <=valor_disponivel
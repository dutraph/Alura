
class Cliente:
    
    def __init__(self, nome, cpf, profissao, endereco):
        self._nome = nome
        self.cpf = cpf
        self.profissao = profissao
        self.endereco = endereco
    

    @property
    def nome(self):
        print("Chamando getter @property nome()")
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        print("Chamando setter nome")
        self._nome = novo_nome

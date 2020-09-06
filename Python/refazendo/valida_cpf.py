class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False # poderia ser Pessoa no lugar de __class__

pe = Pessoa('0000001', 'Ruby')
print(pe.valida_cpf())

pe = Pessoa('00001000000', 'Cristal')
print(pe.valida_cpf())
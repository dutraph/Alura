class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes +=1

    @property
    def nome(self):
        return self._nome.title()
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # Chama o init da class mãe
        self.duracao = duracao
        super().dar_like()


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada
        super().dar_like()

vingadores = Filme("vingadores - gerra infinita", 2018, 160)

print(f' Nome: {vingadores.nome} | Ano: {vingadores.ano} | Duraçao: {vingadores.duracao} mins., Likes {vingadores.likes}  ')
atlanta = Serie("atlanta",2017, 4 )



print(f' Nome: {atlanta.nome} | Ano: {atlanta.ano} | Duraçao: {atlanta.temporada}, Likes {atlanta.likes}.  ')

lista_filme_serie = [vingadores, atlanta]

for i in lista_filme_serie:
    detalhe = i.duracao if hasattr(i, "duracao") else i.temporada  # if ternario em uma linha só
    print(f' Nome: {i.nome} | Ano: {i.ano} | Duraçao: {detalhe}, Likes {i.likes}.  ')
    
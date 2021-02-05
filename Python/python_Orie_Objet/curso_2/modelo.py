class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self._nome} - {self.ano}: {self._likes} Likes'

class Filmes(Programa):
    def __init__(self, nome, ano, duraçao):
        super().__init__(nome, ano)
        self.duraçao = duraçao

    def __int__(self):
        if self.dar_like() == 1:
            like = 'Like'
        else:
            like = 'Likes'
        return f'{self._nome} - {self.ano} - {self.duraçao} min, {self._likes} Likes'

class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __int__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas, {self._likes} Likes'

class Playlist:
    def __int__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)
vingadores = Filmes('vingadores - guerra infinita', 2019, 160)
atlanta = Series('atlanta', 2018, 2)
tmep = Filmes('todo mundo em panio', 1999, 100)
demolidor = Series('demolidor', 2016, 2)
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fds = Playlist('fim de semana', filmes_e_series)

for i in playlist_fds.programas:
    print(i)

'''
ask = int(input('Deseja cadastrar (1)filme ou (2)serie: '))
if ask == 1:
    filme,ano,duraçao = input('Filme: , Ano: , Duraçao: ').split(',')
    a = Filmes(filme, ano, duraçao)
    a.dar_like()
    a.dar_like()
    print(f'Nome: {a.nome}')
    print(f'Ano: {a.ano}')
    print(f'Duração: {a.duraçao}')
    print(f'Likes {a.likes}.')
elif ask == 2:
    nome,ano,temporada = input('Serie: , Ano: , temps: ').split(',')
    a = Series(nome, ano, temporada)
    a.dar_like()
    print(f'Nome: {a.nome}')
    print(f'Ano: {a.ano}')
    print(f'Temporadas: {a.temporadas}')
    print(f'Likes {a.likes}')
else:
    print('Tchau!')
 
'''
from turtle import fd


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

    def __str__(self): #usando o metodo especial __str__ nao precisamos dar um nome ao metodo
        likes = ""
        if(self._likes == 1):
            likes = "Like" 
        else:
            likes = "Likes"
        return f' Nome: {self._nome} | Duraçao: {self.ano} | {likes} {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # Chama o init da class mãe
        self.duracao = duracao

    def __str__(self): #usando o metodo especial __str__ nao precisamos dar um nome ao metodo
        likes = ""
        if(self._likes == 1):
            likes = "Like" 
        else:
            likes = "Likes"
        return f' Nome: {self._nome} | Duraçao: {self.duracao} | Ano: {self.ano} | {likes} {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self): #usando o metodo especial __str__ nao precisamos dar um nome ao metodo
        if self.temporada == 1:
            temps = "Temporada"
        else:
            temps = "Temporadas"
            likes = ""
        if(self._likes == 1):
            likes = "Like" 
        else:
            likes = "Likes"
        return f' Nome: {self._nome} | Temp.: {self.temporada} {temps} | Ano: {self.ano} | {likes} {self._likes}'

class Playlist: 
    def __init__(self,nome, programas):
        self.nome = nome;
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)

vingadores = Filme("vingadores - gerra infinita", 2018, 160)
tmep = Filme("Todo mundo em panico", 1999, 100)
# print(f' Nome: {vingadores.nome} | Ano: {vingadores.ano} | Duraçao: {vingadores.duracao} mins., Likes {vingadores.likes}  ')
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()




atlanta = Serie("atlanta",2017, 1 )
demolidor = Serie("demolidor",2016, 3 )
# print(f' Nome: {atlanta.nome} | Ano: {atlanta.ano} | Duraçao: {atlanta.temporada}, Likes {atlanta.likes}.  ')
atlanta.dar_like()
atlanta.dar_like()

demolidor.dar_like()



lista_filme_serie = [vingadores, atlanta, demolidor, tmep]
playlist_fds = Playlist('fim de semana', lista_filme_serie)

print(f'Tamanho da playlit {len(playlist_fds.listagem)}')

for i in playlist_fds:
    print(i)

    # detalhe = i.duracao if hasattr(i, "duracao") else i.temporada  # if ternario em uma linha só
    # print(f' Nome: {i.nome} | Ano: {i.ano} | Duraçao: {detalhe}, Likes {i.likes}.  ')


class Filmes:
    # Função contrutora
    def __init__(self, nome, ano, duraçao):
        self.__nome = nome.title()
        self.ano = ano
        self.duraçao = duraçao
        self.__likes = 0
    
    @property
    def likes(self):
        return self.__likes
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1
    


class Series:
    # Função contrutora
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1
       

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
    nome,anoserie,temporada = input('Serie: , Ano: , temps: ').split(',')
    a = Series(nome, anoserie, temporada)
    a.dar_like()
    a.dar_like()
    print(f'Nome: {a.nome} | Ano: {a.ano} | Temporadas: {a.temporadas} | Likes {a.likes}')
else:
    print('Tchau!')
'''def palavra_secreta():
    
    lista_eletronico = ['impressora', 'celular', 'tablet', 'computador']

    tipo = input('Escolha o tipo de palavra, (1)frutas  ou (2)eletronicos: ')
    if tipo == '1':
        escolha_random = random.choice(lista_fruta)
    elif tipo == '2':
        escolha_random = random.choice(lista_eletronico)

if(__name__ == '__main__'):
    palavra_secreta()


'''
'''
nomeIdade = {'Paulo' : 29, 'Maria' : 27, 'Marcos' : 52}

print(nomeIdade['Maria'])
print(nomeIdade['Maria'])'''









import random
lista_fruta = ['banana', 'uva', 'abacate', 'melao']
numero = random.randrange(0, len(lista_fruta))
palavra_secreta = lista_fruta[numero].upper()
print(palavra_secreta)
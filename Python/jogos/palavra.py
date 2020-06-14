def palavra_secreta():
    import random
    lista_fruta = ['banana', 'uva', 'abacate', 'melao']
    lista_eletronico = ['impressora', 'celular', 'tablet', 'computador']

    tipo = input('Escolha o tipo de palavra, (1)frutas  ou (2)eletronicos: ')
    if tipo == '1':
        escolha_random = random.choice(lista_fruta)
    elif tipo == '2':
        escolha_random = random.choice(lista_eletronico)

    print(escolha_random)

if(__name__ == '__main__'):
    palavra_secreta()


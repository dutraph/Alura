palavra = input('Palavra: ')
size = len(palavra)
lista = []
lista.append(size * '_ ')
c = 1
while c <= size:
    c = c + 1
    letra = input(f'Entre o {c} valor: ')
    lista.append(letra)

print(lista)
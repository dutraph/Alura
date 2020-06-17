preco = []
c = 0
while c <= 2:
    c = c + 1
    valor = float(input(f'Entre o {c} valor: '))
    preco.append(valor)

print(f'O menor valor eh {min(preco)}')
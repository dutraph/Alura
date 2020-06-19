Funcao count()
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))

O código acima nos retorna 3, pois em nossa lista encontramos 3 vezes o número zero nela.

letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))


Funcao index()
frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))

O código acima nos retorna 3, pois é o índice da primeira ocorrência do elemento 'Uva' na lista frutas (lembre-se nas listas começamos a contar do índice 0).


frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
print(frutas.index('Melancia'))

Ao tentar buscar pela fruta 'Melancia', obteremos o erro "ValueError: 'Melancia' is not in list"

frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:   
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))

    Assim temos certeza que a fruta_buscada está dentro da lista antes de perguntarmos o seu índice, evitando assim de receber um erro no console.
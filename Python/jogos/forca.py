def jg_forca():
    import getpass
    print("***********************")
    print("  Bem vindo ao Forca!  ")
    print("***********************", end="\n\n")

    #palavra_secreta,tipo = input('Qual a palavra e o tipo: ').split()
    #print(f'Dica: a palavra secreta tem {len(palavra_secreta)} letras, e eh um(a) {tipo}. Boa sorte.')
    palavra_secreta = getpass.getpass('Digite a palavra secreta: ')
    size = len(palavra_secreta)
    print(f'Dica: a palavra tem {size} letras')
    letras_acertadas = ['_', '_', '_', '_']
    #letras_acertadas.append(size * ('_',))
    enforcou = False
    acertou = False
    # enquanto True e True 
    while not enforcou and not acertou:
        
        chute = input('Qual letra?: ')
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra
                print(f'Encontrei a letra "{letra}" na posicao {index}.')
            index = index + 1
        print(letras_acertadas)

    print('Fim do Jogo')

if(__name__ == '__main__'):
    jg_forca()
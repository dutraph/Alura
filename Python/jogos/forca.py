def jg_forca():
    import getpass
    import palavra
    print("***********************")
    print("  Bem vindo ao Forca!  ")
    print("***********************", end="\n\n")

    #palavra_secreta,tipo = input('Qual a palavra e o tipo: ').split()
    #print(f'Dica: a palavra secreta tem {len(palavra_secreta)} letras, e eh um(a) {tipo}. Boa sorte.')

    palavra_secreta = palavra.palavra_secreta()
    '''palavra_secreta = getpass.getpass('Digite a palavra secreta: ').upper()
    size = len(palavra_secreta)
    print(f'Dica: a palavra tem {size} letras')
    '''
    #letras_acertadas = []
    #for i in range(size):
    #   letras_acertadas.append('_')
    # OU
    print(palavra_secreta)
    letras_acertadas = ['_' for letra in palavra_secreta]

    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0
    # enquanto True e True 
    while not enforcou and not acertou:
        
        chute = input('Qual letra?: ')
        chute = chute.strip().upper()
    

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                    print(f'Encontrei a letra "{letra}" na posicao {index}.')
                index += 1 
            
        else:
            erros += 1
        acertou = '_' not in letras_acertadas
        enforcou = erros == size    
        print(letras_acertadas)
        print(f'Faltam {size - erros} tentativas.')
    if acertou:
        print('Voce venceu!')
    else:
        print('Voce perdeu')

    print('Fim do Jogo')

if(__name__ == '__main__'):
    jg_forca()
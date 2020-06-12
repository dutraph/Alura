def jg_forca():
    print("***********************")
    print("  Bem vindo ao Forca!  ")
    print("***********************", end="\n\n")

    palavra_secreta,tipo = input('Qual a palavra e o tipo: ').split()
    print(f'Dica: a palavra secreta tem {len(palavra_secreta)} letras, e eh um(a) {tipo}. Boa sorte.')
    
    enforcou = False
    acertou = False
    # enquanto True e True 
    while not enforcou and not acertou:
        lista = []
        chute = input('Qual letra?: ')
        chute = chute.strip()

        lista = []
        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print(f'Encontrei a letra "{letra}" na posicao {index}.')
            index = index + 1
        print('Jogando...')

    print('Fim do Jogo')

if(__name__ == '__main__'):
    jg_forca()
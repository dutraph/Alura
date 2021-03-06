def jogar():
    import getpass
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = getpass.getpass('Digite a palavra secreta: ').upper()
    size = len(palavra_secreta)
    print(f'Dica: a palavra tem {size} letras')
    
    letras_acertadas = []
    for i in range(size):
        letras_acertadas.append('_')
    print(type(palavra_secreta))
    print(letras_acertadas)

    erros = 0
    while(True):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        if (erros == 6):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)
        print(f'Faltam {size - erros} tentativas.')

    if("_" not in letras_acertadas):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim do jogo")

if __name__ == "__main__":
    jogar()
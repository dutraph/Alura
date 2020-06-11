def jg_forca():
    print("**********************")
    print("Bem vindo ao Forca!")
    print("**********************", end="\n\n")

    sec_word = "banana"
    tentativas = 0
    nivel = int(input("Escolha a dificuldade do jogo.(1) Fácil  (2) Médio  (3) Difícil: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    enforcou = False
    acertou = False

    # enquanto (True and True) 
    while not enforcou and not acertou:

        chute = input("Digite uma letra: ")

        index = 0
        for letra in sec_word:
            if chute == letra:
                print("A letra {} estra na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas, end="\n\n"))

    print("Fim!")

if __name__ == "__main__":
    jg_forca()
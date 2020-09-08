from random import randint
import os
def limpar():
    os.system('clear')
def jogar():
    limpar()
    print("*************")
    print("Adivinhação")
    print("*************")

    level = int(input("Choose your level: 1 (easy) | 2 (medium) | 3 (hard) "))

    num_sec = randint(1, 100)
    pts = 1000
    if (level == 1):
        limpar()
        total_tries = 12
        dica_menor = num_sec - 4
        dica_maior = num_sec + 7
        print(f"Dica: o numero secretro esta entre {dica_menor} e {dica_maior} ")
    elif (level == 2):
        limpar()
        dica_menor = num_sec - 8
        dica_maior = num_sec + 11
        print(f"Dica: o numero secretro esta entre {dica_menor} e {dica_maior} ")

        total_tries = 6
    elif (level == 3):
        limpar()
        print("O numero secreto esta entre 1 e 100, boa sorte. Muahahahaha")
        total_tries = 3

    else:
        print("Invalid option, please try again!")

    #rodada = 1 #so precisa ser usado no while

    print("Voce começa com 100 pontos.")
    print(num_sec)
    for rodada in range(1, (total_tries+1)):
        
        print(f"Tentativa {rodada} de {total_tries}.")
        chute = int(input("Digite seu chute: "))
        limpar()
        if (chute < 1 or chute >100):
            print("chute entre 1 e 100")
            continue

        acertou = chute == num_sec
        maior = chute > num_sec
        menor = chute < num_sec

        if(acertou):
            print("voce acertou")
            break
        else:
            if(maior):
                print("Voce errou, seu chute foi maior que o numero secreto")
            elif(menor):
                print("Voce errou, seu numero foi menor que o numero secreto")
            pontos_perdidos = abs(num_sec - chute)
            pts = pts - pontos_perdidos
    limpar()
    print(f"Sua pontuaçao é: {pts}")
    print("Fim do jogo!")
if(__name__ == '__main__'):
    jogar()


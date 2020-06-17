import forca
import adv
def escolhe_jogos():
    print("**********************")
    print("*  Escolha um jogo!  *")
    print("**********************", end="\n\n")

    jogo = int(input("(1) Forca | (2) Adivinhação | (3)Sair: "))

    if jogo == 1:
        print("Jogando Forca!")
        forca.jg_forca()
    elif jogo == 2:
        print("Jogando Adivinhação")
        adv.jg_adv()
    else:
        print('Ate logo!')
if __name__ == "__main__":
    escolhe_jogos()
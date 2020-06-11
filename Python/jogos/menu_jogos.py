import forca
import adv
def escolhe_jogos():
    print("**********************")
    print("*  Escolha um jogo!  *")
    print("**********************", end="\n\n")

    jogo = int(input("(1) Forca | (2) Adivinhação: "))

    if jogo == 1:
        print("Jogando Forca!")
        forca.jg_forca()
    elif jogo == 2:
        print("Jogando Adivinhação")
        adv.jg_adv()

if __name__ == "__main__":
    escolhe_jogos()
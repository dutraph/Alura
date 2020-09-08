import forca
import adivinha
import os
os.system('clear')
def escolhe_jogo():
    print("*************")
    print("Menu de Jogos")
    print("*************")

    jogo = int(input("Qual jogo quer jogar: 1 (Forca) | 2 (Adivinhaçao) | 3 (sair) "))

    if jogo == 1 :
        print("Jogando Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando Adivinhaçao")
        adivinha.jogar()
    else:
        print("Ate logo")

if(__name__ == '__main__'):
    escolhe_jogo()
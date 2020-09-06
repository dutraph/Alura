import random
import os
def limpar():
    os.system('clear')
def jogar():
    limpar()
    print("*************")
    print("Jogo da forca")
    print("*************")

    palavras = []
    with open('frutas.txt', 'r') as arquivo: # USANDO O WITH NAO PRECISA FAZER arquivo.close()
        for linha in arquivo:
            palavras.append(linha.strip().upper())
    palavra_secreta = (random.choice(palavras))

    print(palavras)
    enforcou = False
    acertou = False
    erros = 0
    letra_acertadas = ["_" for letra in palavra_secreta]
    # for letra in palavra_secreta:
    #     letra_acertadas.append("_")
    print(letra_acertadas)

    while(not enforcou and not acertou):
        tentativas = len(palavra_secreta)
        chute = input("Qual letra: ")
        chute = chute.upper().strip()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letra_acertadas[index] = letra
                index += 1
                
        else:
            erros += 1
            print(f"Ops, vc errou, restam: {tentativas - erros} tentativas")
        enforcou = erros==len(palavra_secreta)
        acertou = "_" not in letra_acertadas
        print(letra_acertadas)
    if(acertou):
        print("Voce Ganhou")
    else:
        print("Voce perdeu")
if(__name__ == '__main__'):
    jogar()
import random
import menu_jogos

def mensagem_abertura():
    print("***********************")
    print("  Bem vindo ao Forca!  ")
    print("***********************", end="\n\n")

def carrega_pal_sec():

    palavras = []
    with open('frutas.txt', 'r') as arquivo:
        for i in arquivo:
            palavras.append(i.strip())
    palavra_secreta = (random.choice(palavras)).upper()
    #size = len(palavra_secreta)
    return palavra_secreta

def carrega_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    chute = input('Qual letra?: ')
    chute = chute.strip().upper()
    return chute

def chute_certo(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
            print(f'Encontrei a letra "{letra}" na posicao {index}.', end='\n\n')
        index += 1

def msg_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def msg_perdedor(palavra_secreta):
    print("Você foi enforcado!")
    print(f"A palavra era {palavra_secreta}!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def restart_jogo():

    askJogar = int(input('Deseja jogar novamente: (1)Forca (2)Menu de Jogos (3)Sair.'))
        
    if askJogar == 1:
        jg_forca()
    elif askJogar == 2:
        menu_jogos.escolhe_jogos()
    else:
        print('Até logo!')

def jg_forca():

    mensagem_abertura()
    palavra_secreta = carrega_pal_sec()
    letras_acertadas = carrega_letras_acertadas(palavra_secreta)
    print(letras_acertadas) 

    size = len(palavra_secreta)
    print(f'Dica: a palavra tem {size} letras. e é uma Fruta.', end='\n\n')

    enforcou = False
    acertou = False
    erros = 0
    while not enforcou and not acertou:
        
        chute = pede_chute()
    
        if chute in palavra_secreta:
            chute_certo(chute, letras_acertadas, palavra_secreta)        
        else:
            erros += 1
            desenha_forca(erros)

        acertou = '_' not in letras_acertadas
        enforcou = erros == 7    
        print(letras_acertadas)
        print(f'Faltam {7 - erros} tentativas.')
    if acertou:
        msg_vencedor()
    else:
        msg_perdedor(palavra_secreta)

    print('Fim do Jogo', end='\n\n')
    restart_jogo()                

if(__name__ == '__main__'):
    jg_forca()
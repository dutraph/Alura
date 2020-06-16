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

def jg_forca():

    mensagem_abertura()
    # ESCOLHA ALEATORIA DA PALVRA E TIPO 
    palavra_secreta = carrega_pal_sec()
    size = len(palavra_secreta)
    print(f'Dica: a palavra tem {size} letras. e é uma Fruta.', end='\n\n')
    # GERANDO ESPAÇOS VAZIOS
    letras_acertadas = ['_' for letra in palavra_secreta]  
    print(letras_acertadas) # OU 
    #letras_acertadas = []
    #for i in range(size):
    #   letras_acertadas.append('_')

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
                    print(f'Encontrei a letra "{letra}" na posicao {index}.', end='\n\n')
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

    print('Fim do Jogo', end='\n\n')
    askJogar = int(input('Deseja jogar novamente: (1)Forca (2)Menu de Jogos.'))
    if askJogar == 1:
        jg_forca()
    else: 
        menu_jogos.escolhe_jogos()
            
        

if(__name__ == '__main__'):
    jg_forca()
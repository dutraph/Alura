from random import randint
import menu_jogos
def jg_adv():

    print("**********************")
    print("Bem vindo ao adivinha!")
    print("**********************", end="\n\n")

    sec_num = (randint(0, 5))
    tentativas = 0
    pts = 100
    nivel = int(input("Escolha a dificuldade do jogo.(1) Fácil  (2) Médio  (3) Difícil: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    elif nivel == 3:
        tentativas = 5
    else:
        print("Operação invalida")

    for rodada in range(1, tentativas + 1):
        print(f"Tentativa {rodada} de {tentativas}", end="\n\n")
        chute = int(input("Digite um número entre 1 e 5: "))
        print("Seu chute foi: ", chute, end="\n\n")

        if chute < 0 or chute > 5:
            print("Alerta! Voce deve digitar um numero entre 0 e 5", end="\n\n")
            continue

        certo = sec_num == chute
        maior = chute > sec_num
        menor = chute < sec_num

        if certo:
            print(f"Voce acertou! Sua pontuaçao foi {pts:.02f}")
            break
        else:
            if maior:
                print("Errou, o chute foi maior que o numero secreto!", end="\n\n")
            elif menor:
                print("Errou, o chute foi menor que o numero secreto!", end="\n\n")
            pts_perd = abs(sec_num - chute) / 3
            pts = pts - pts_perd

    print("Fim!")
    askJogar = int(input('Deseja jogar novamente: (1)Adivinha (2)Menu de Jogos (3)Sair.'))
    if askJogar == 1:
        jg_adv()
    elif askJogar == 2:
        menu_jogos.escolhe_jogos()
    else: 
        print('Ate logo!')
        
if __name__ == "__main__":
    jg_adv()



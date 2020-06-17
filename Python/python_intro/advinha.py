print("**********************")
print("Bem vindo ao Cara ou Coroa!")
print("**********************")

nome = input("Qual seu nome: ")
def jg():
    from random import randint
    sec_num = (randint(0,1))
    chute = int(input("Digite (0 para Cara) e (1 para Coroa): "))

    if(sec_num == chute and chute == 0):
        print("Cara", end="\n\n")
    else:
        print("Coroa", end="\n\n")

    replay = str(input("Deseja jogar novamente?[s/n]: "))

    if(replay == "s"):
        jg()
    else:
        print("Ate logo!")
jg()

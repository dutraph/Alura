print("**********************")
print("Bem vindo ao adivinha!")
print("**********************")

nome = input("Qual seu nome: ")
def jg():
    from random import randint
    sec_num = (randint(0,1))
    chute = int(input("Digite um numero de 0 a 1: "))

    if(sec_num == chute):
        print("Parabens %s, voce acertou" %nome, end="\n\n")
    else:
        print("Voce errou!!!", end="\n\n")

    replay = str(input("Deseja jogar novamente?[s/n]: "))

    if(replay == "s"):
        jg()
    else:
        print("Ate logo!")
jg()

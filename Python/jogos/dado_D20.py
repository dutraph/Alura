from random import randint

def dado20():
    n = randint(1,20)
    if (n == 20):
        print(f'{n} Critical.')
    else:
        print(n)

def dado6():
    n = randint(1, 6)
    print(n)
dado20()

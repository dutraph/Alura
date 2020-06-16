'''arquivo = open("frutas.txt", "w")
arquivo
frutas = ["maçã ", "banana ", "laranja ", "melancia "]
for fruta in frutas:
    arquivo.write(fruta)
arquivo.close()


arquivo = open('frutas.txt', 'r')
arquivo2 = arquivo.readline()
print(arquivo2.strip())
arquivo2 = arquivo.readline()
print(arquivo2.strip())
arquivo.close()
'''
import random
arquivo = open('frutas.txt', 'r')
palavras = []
for i in arquivo:
    palavras.append(i)

print(random.choice(palavras).strip())
arquivo.close()
'''arquivo = open("frutas.txt", "w")
arquivo
frutas = ["maçã ", "banana ", "laranja ", "melancia "]
for fruta in frutas:
    arquivo.write(fruta)
arquivo.close()
'''
arquivo = open('frutas.txt', 'r')
arquivo
for i in arquivo:
    print(i)
arquivo.close()
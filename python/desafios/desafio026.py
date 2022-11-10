#Faça um programa que leia uma frase pelo teclado e mostre:

#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input("Digite uma frase aleatória: ")).strip()

frase = frase.lower()

print("Quantas vezes aparece a letra A?: {} vezes.".format(frase.count("a")))
print("Em que posição ela aparece a primeira vez?: {}".format(frase.find("a")+1))
print("Em que posição ela aparece a última vez?: {}".format(frase.rfind("a"))+1)
print(len(frase))
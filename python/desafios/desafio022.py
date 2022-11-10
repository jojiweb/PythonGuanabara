#Crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input("Digite seu nome completo: ").strip()

separa = nome.split()

print("Letras Maiúsculas: {}".format(nome.upper()))
print("Letras Minúsculas: {}".format(nome.lower()))

nome = nome.replace(" ", "")

print("Quantas Letras: {}".format(len(nome)))
print("Primeiro Nome Letras: {}".format(len(separa[0])))
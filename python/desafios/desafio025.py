#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input("Digite seu nome completo: ")

nome = nome.lower()

print("Seu nome tem Silva?: {}".format("silva" in nome))
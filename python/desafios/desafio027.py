#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

#Ex: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

nome = input("Digite seu nome completo: ")

nomeLista = nome.split()

print("Primeiro nome: {}".format(nomeLista[0]))
print("Último nome: {}".format(nomeLista[len(nomeLista)-1]))

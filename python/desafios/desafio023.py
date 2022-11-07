#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#Ex: digite um número: 1834

#unidade:4 dezena:3 centena:8 milhar:1

numero = input("Digite um número de 0 a 9999: ")
dezena = numero[-1:3]

print("Unidade: {}".format())
print("Dezena: {}".format())
print("Centena: {}".format())
print("Milhar: {}".format())
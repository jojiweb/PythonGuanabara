#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
    
n = int(input(("Digite um número: ")))
    
resto = n % 2

if resto == 0:
    print("O número é PAR!")
else:
    print("O número é ÍMPAR!")    
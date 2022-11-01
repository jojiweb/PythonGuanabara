# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.



n1 = int(input("Um valor: "))

sucessor = n1 + 1 
antecessor = n1 - 1

print("O sucessor de {} é {} e o antecessor é {}".format(n1, sucessor, antecessor))
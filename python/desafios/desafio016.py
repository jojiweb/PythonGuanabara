# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: 6.127 = 6

from math import trunc
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, trunc(num)))
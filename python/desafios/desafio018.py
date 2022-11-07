# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.   

from math import sin, cos, tan, radians

an = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print("O ângulo de {} tem o SENO de {:.2f}".format(an, seno))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(an, cosseno))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(an, tangente))
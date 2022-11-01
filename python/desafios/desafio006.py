# Crie um algoritmo que leia um número e mostre o seu dobro e raiz quadrada.

n1 = int(input("Um valor: "))

dobro = n1*2
triplo = n1 * 3
raizQuadrada = n1 ** (1/2)


print("O dobro é {} \nO triplo é {} \nA raiz quadrada é {:.2f}".format(dobro, triplo, raizQuadrada))
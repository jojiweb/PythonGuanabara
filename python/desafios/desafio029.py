#Escreva um programa que leia a velocidade de um carro

#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custa R$7,00 por cada Km acima do limite.

vm = 80

km = int(input("A quantos quilômetros você passou?: "))

if km > 80:
    multa = (km - 80) * 7
    print("Você foi multado! Sua multa é de R${}".format(multa))
else:
    print("Você não foi multado, parabéns!")
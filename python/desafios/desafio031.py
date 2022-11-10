#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km a R$0,45 para viagens mais longas.

distancia = int(input("Digite a distância da viagem em KM: "))

if distancia <= 200:
    preço = distancia * 0.50
    print("O preço vai ser {}.".format(preço))
else:
    preço = distancia * 0.45
    print("O preço vai ser {}.".format(preço))
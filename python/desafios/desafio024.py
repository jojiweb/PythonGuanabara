#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input("Digite o nome de uma cidade: ")

cidade = cidade.lower()
lista = cidade.split()
print("A cidade começa com SANTO?: {}".format("santo" in lista[0]))
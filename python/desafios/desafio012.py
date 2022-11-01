# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n1 = float(input("Digite um preço: R$"))


porcentagem = n1*5/100
novoPreco = n1 - porcentagem

print("O preço desse produto de acordo com o novo desconto é {:.2f}".format(novoPreco))
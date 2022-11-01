# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

n1 = float(input("Digite o salário: R$"))


porcentagem = n1 * 15 / 100
novoSalario = n1 + porcentagem

print("O seu salário com 15%' de aumento agora é R${:.2f}".format(novoSalario))
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

#Para salários superiores a R$1.250,00 calcule um aumento de 10%

#Para os inferiores ou iguais, o aumento é de 15%.

s = float(input("Salário: "))

if s >= 1.250:
    porcentagem = s * 15 / 100
    ns = s + porcentagem
    print("Seu novo salário é: R${:.2f}".format(ns))
else:
    porcentagem = s * 10 / 100
    ns = s + porcentagem
    print("Seu novo salário é: R${:.2f}".format(ns))
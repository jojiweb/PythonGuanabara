nome = input("Seja bem-vindo(a)! Qual o seu nome? ")
n1 = int(input("Olá, {:=^15}. Digite um número: ".format(nome)))
n2 = int(input("Digite outro número: "))

soma = n1 + n2
divisao = n1 / n2
divisaoInteira = n1 // n2
multiplicacao = n1 * n2
potencia = n1**n2

print("Aqui estão os resultados: \n a SOMA desses números é {} \n A DIVISÃO desses números é {} \n A DIVISÃO INTEIRA desses números é {} \n A multiplicação desses números é {} \n A POTÊNCIA desses números é {}".format(soma, divisao, divisaoInteira, multiplicacao, potencia))
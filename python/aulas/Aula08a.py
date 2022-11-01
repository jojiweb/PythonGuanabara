from math import sqrt, floor

n1 = int(input("Digite um número para a raiz quadrada: "))
raiz = sqrt(n1)

print("A raiz quadrada de {} é {:.2f}".format(n1, floor(raiz)))
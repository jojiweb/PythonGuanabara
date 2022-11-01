# Escreva um programa que converta uma temperatura digitada em C e converta para F

c = float(input("Escreva os graus em celsius: "))

f = c * 1.8 + 32.00

print("{}C são {}F".format(c, f))
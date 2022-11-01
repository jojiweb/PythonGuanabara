# Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetro

n1 = float(input("Um valor: "))

cen = n1 * 100
mili = n1 * 1000

print("{} metros tem {} centímetros e {} milímetros.".format(n1, cen, mili))


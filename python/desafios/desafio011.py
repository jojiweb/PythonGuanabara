# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input("Digita a altura da parede em metros: "))
largura = float(input("Digita a largura da parede em metros: "))

area = largura * altura
tinta = area / 2

print("Sua parede tem a dimensão de {} X {} e sua área é de {}m²".format(altura, largura, area))
print("Você precisará de {}L litros de tinta para pintar a parede.".format(tinta))
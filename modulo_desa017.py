import math

catum = float(input("Digite o valor do cateto adjacente: "))
catdois = float(input("Digite o valor do cateto oposto: "))

hipsemraiz = math.sqrt(catum ** 2 + catdois ** 2)

print(f"A hipotenuza do triangulo é: {hipsemraiz}")
import math

angulo = float(input("Digite o valor do angulo que deseja saber o cosseno, seno e tangente: "))

anguloradiano = angulo * math.pi / 180

cos = math.cos(anguloradiano)

sen = math.sin(anguloradiano)

tang = math.tan(anguloradiano)


print(f"O valor do cosseno de {angulo} é {cos}, já a tangente é {tang} e o senno vale {sen}")
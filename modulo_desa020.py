import random

al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))

lista = [al1,al2, al3, al4]
aluno_escolhido = random.choice(lista)
print(f"O aluno escolhido foi {aluno_escolhido}")
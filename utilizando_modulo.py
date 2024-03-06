#modulos são elementos importados, por exemplo importar bibliotecas que terão funções.
#para importar todos os itens da biblioteca a escrita fica "import(biblioteca)"
#para importar apenas um dado em especifico from(biblioteca(import)(funcao))

#função ceil(arredonda), floor(arredonda pra baixo), trunc(eliminar a virgula pra frente, pow(potencia)
#sqrt(raiz quadrada), factorial(fatora)
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')

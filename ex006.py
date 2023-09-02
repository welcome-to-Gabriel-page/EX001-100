# programa q solicita um numero o imprime o dobro, triplo e raiz quadrada do mesmo #6

import math

numero = (int(input('Digite um número: ')))
raizQuadrada = int(math.sqrt(numero))
print('O dobro de {} é {}'.format(numero, (numero+numero)))
print('O triplo de {} é {}'.format(numero, (numero*3)))
print('A raiz quadrada de {} é {}'.format(numero, raizQuadrada))












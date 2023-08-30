# exercicio para ler o peso de 5 pessoas e definir o maior e o menor peso


maiorPeso = 0
menorPeso = 0

for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('O maior peso lido foi {}KG'.format(maiorPeso))
print('O menor peso lido foi {}KG'.format(menorPeso))



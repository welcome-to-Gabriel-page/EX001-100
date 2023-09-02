# refazendo a tabuada que fizemos no ex09 de uma forma muito mais prática #14

numero = int(input('Digite um número: '))
for contador in range(1, 11):
    print('{} x {} = {}'.format(numero, contador, contador*numero))

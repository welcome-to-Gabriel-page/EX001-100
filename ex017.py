numeroInteiro = int(input('Digite um número: '))
total = 0
for contador in range(1, numeroInteiro + 1):
    if numeroInteiro % contador == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(contador), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(numeroInteiro, total))
if total == 2:
    print('E por isso ele é um número PRIMO')
else:
    print('E por isso ele NÃO É um número PRIMO')


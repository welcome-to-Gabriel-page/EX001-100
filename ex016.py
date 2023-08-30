primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao
for contador in range(primeiro, decimo + razao, razao):
    print('{} '.format(contador), end='> ')
print('OVER')



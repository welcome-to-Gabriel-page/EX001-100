# contador 0 a 500
# quantidade de valores multiplos de 3
# soma dos multiplos de 3
#13


soma = 0
const = 0
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        const = const + 1 # const += 1
        soma = soma + contador # soma += contador
print('A soma dos {} múltiplos encontrados, de 0 a 500 é: {}'.format(const, soma))


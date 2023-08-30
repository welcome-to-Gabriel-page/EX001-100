# solicitar 6 numeros inteiros
# resgatar apenas numeros pares
# somar a quantidade de numeros pares encontrados e a soma entre eles

contador = 0
soma = 0

for c in range(1,7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        contador += 1
        soma += numero
print('A soma dos {} números pares informados é: {}'.format(contador, soma))





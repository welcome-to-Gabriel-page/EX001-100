# exercicio para pegar nome idade e sexo de 4 pessoas
# calcular a media da idade de toda as 4 pessoas
# mostrar idade e nome do homem mais velho
# mostrar quantas mulheres menores de 20 anos existem no grupo
#20

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeMaisVelho = ''
totalMulher20 = 0

for pessoa in range(1, 5):
    print('-------{} PESSOA-------'.format(pessoa))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo M/F: ')).strip() .upper()
    somaIdade += idade
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher20 += 1

mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeMaisVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalMulher20))





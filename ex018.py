# exercicio para verificar idade e se é maior ou menor de 18 #18

from datetime import date
atual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoa in range(1,8):
    nascimento = int(input('Em que ano a {} pessoa nasceu?'.format(pessoa)))
    idade = atual - nascimento
    if idade >= 18:
        totalMaior += 1
    else:
        totalMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalMaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totalMenor))

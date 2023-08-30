# calculo de medias dos alunos
# autor: gabriel paiva

print('Sistema de cálculo da média, utilizando prova 1 e prova 2')
print('Cadastre sua nota: ')
prova1 = float(input('Digite a nota 1: '))
prova2 = float(input('Digite a nota 2: '))

media = (prova1 + prova2)/2.0

if (media <= 4.0):
    print('O aluno está reprovado! média: {}'.format(media))

if (media > 4.0 and media < 7.5):
    print('O aluno está de recuperação! média {}'.format(media))

if (media >= 7.5):
    print('O aluno está aprovado! média {}'.format(media))




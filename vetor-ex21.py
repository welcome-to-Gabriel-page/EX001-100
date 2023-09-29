# programa para calcular a soma e a média de 3 notas de um aluno

notas = [0.0, 0.0, 0.0]
notas[0] = float(input('Informe a primeira nota: '))
notas[1] = float(input('Informe a segunda nota: '))
notas[2] = float(input('Informe a terceira nota: '))

somaNotas = notas[0] + notas[1] + notas[2]
mediaNotas = somaNotas/3.0

print('Relatório das notas do aluno:')
print('Notas: {}'.format(notas))
print('Soma: {}'.format(somaNotas))
print('Media: {}'.format(mediaNotas))

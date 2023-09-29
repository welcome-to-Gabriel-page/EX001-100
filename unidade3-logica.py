# Função em Python que implementa as regras de negócio
# Autor: Gabriel de Paiva Silva


def aprovar(notaProva, notaTrabalhos, frequencia):
    if notaProva > 7:
        return 'A nota máxima da prova é 7.'
    elif notaTrabalhos > 3:
        return 'A nota máxima para trabalhos é 3.'
    elif notaProva + notaTrabalhos >= 7 and frequencia >=75:
        return 'Aprovado'
    else:
        return 'Reprovado'


def main():
    notaProva = float(input('Digite a nota da prova de 0 a 7: '))
    notaTrabalhos = float(input('Digite a nota dos trabalhos de 0 a 3: '))
    frequencia = float(input('Digite a frequência em %'))

    resultado = aprovar(notaProva, notaTrabalhos, frequencia)
    print(f'Situação do aluno: {resultado}')

if __name__ == '__main__':
    main()




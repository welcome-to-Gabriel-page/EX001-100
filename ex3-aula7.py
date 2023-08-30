# calculo de combustivel em viagem
# autor: gabriel paiva

print('Sistema para calculo de gastos contínuos')
print('Informe os dados da viagem: ')
velocidadeMedia = float(input('Digite a velocidade média: '))
tempoDeViagem = float(input('Digite o tempo de viagem: '))
rendimentoVeiculo = float(input('Digite o rendimento do veículo Km por L'))

distancia = tempoDeViagem*velocidadeMedia
litrosGastos = distancia/rendimentoVeiculo

print()
print('Relatório de viagem: ')
print(tempoDeViagem)
print(distancia)
print(velocidadeMedia)
print(rendimentoVeiculo)
print()
print('consumo: {}'.format(litrosGastos))


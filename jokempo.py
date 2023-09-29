# AUTOR: Gabriel de Paiva Silva

nomeJogadorUm = str(input('Digite seu nome: '))
nomeJogadorDois = str(input('Digite seu nome: '))

pedra = "pedra"
papel = "papel"
tesoura = "tesoura"
empate = "Empate"

pedra.lower()
papel.lower()
tesoura.lower()

def vencedor_perdedor_empate(jogadorUm, jogadorDois):
    if jogadorUm == pedra and jogadorDois == tesoura:
        print('Vencedor: {}'.format(nomeJogadorUm))
    elif jogadorUm == tesoura and jogadorDois == pedra:
        print('Vencedor: {}'.format(nomeJogadorDois))
    elif jogadorUm == tesoura and jogadorDois == papel:
        print('Vencedor: {}'.format(nomeJogadorUm))
    elif jogadorUm == papel and jogadorDois == tesoura:
        print('Vencedor: {}'.format(nomeJogadorDois))
    elif jogadorUm == papel and jogadorDois == pedra:
        print('Vencedor: {}'.format(nomeJogadorUm))
    elif jogadorUm == pedra and jogadorDois == papel:
        print('Vencedor: {}'.format(nomeJogadorDois))
    elif jogadorUm == pedra and jogadorDois == pedra:
        print('Resultado: {}'.format(empate))
    elif jogadorUm == papel and jogadorDois == papel:
        print('Resultado: {}'.format(empate))
    elif jogadorUm == tesoura and jogadorDois == tesoura:
        print('Resultado: {}'.format(empate))
    else:
        print('Você não informou os valores corretamente.')


def main():
    jogadorUm = str(input('Pedra, Papel ou Tesoura?\n: '))
    jogadorDois = str(input('Pedra, Papel ou Tesoura?\n: '))

    resultadoJogo = vencedor_perdedor_empate(jogadorUm, jogadorDois)

if __name__ == '__main__':
    main()
    

    

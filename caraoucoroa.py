# Jogo de azar do Cara ou Coroa
# Autor: Gabriel de Paiva Silva


import random

def caraOuCoroa():
    resultado = random.randint(0, 1)
    
    if resultado == 0:
        return "Cara"
    else:
        return "Coroa"

# funcao principal

def main():
    while True:
        input("Pressione ENTER para lançar a moeda: ")
        
        resultado = caraOuCoroa()
        print('Resultado: {}'.format(resultado))
        
        jogarNovamente = input("Deseja jogar novamente? (s/n): ")
        
        if jogarNovamente.lower() != "s":
            break

if __name__ == "__main__":
    main()

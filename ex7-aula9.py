# condições para achar um triângulo e qual tipo de triângulo #7 aula 9

print("Insira as medidas")
n1 = int(input("Insira a primeira metragem: "))
n2 = int(input("Insira a segunda metragem: "))
n3 = int(input("Insira a terceira metragem: "))
print()
if (n1 < n2 + n3) and (n2 < n1 + n3) and (n3 < n1 + n2):
    print("As metragens formam um triângulo")
    if (n1 == n2 == n3):
        print('tipo: Equilátero')

    if (n1 == n2 != n3):
        print('tipo: Isósceles')

    if (n1**2 + n2**2 == n3**2):
        print('tipo: triângulo retângulo')
else:
    print("As metragens não formam um triângulo")
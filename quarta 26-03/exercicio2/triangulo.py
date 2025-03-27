# 2. Identificação do Triângulo
# Peça ao usuário três valores numéricos e verifique se correspondem a um triângulo e qual seu tipo.
# Faça o fluxograma do algoritmo e depois o escreva em Python.

lado1 = int(input("Digite o valor do lado a: "))
lado2 = int(input("Digite o valor do lado b: "))
lado3 = int(input("Digite o valor do lado c:"))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Triângulo equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")        
else:
    print("Não é um triângulo")
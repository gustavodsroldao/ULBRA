# Verificar se um número é par
# Peça ao usuário um número e faça a verificação se o número é par, imprimido o resultado em tela.
# Desafio Extra: Adapte o código do exercício 3 e verifique também se o número é zero, 
# exibindo uma mensagem específica para essa situação.

numero = int(input("Digite um número: "))
if numero == 0:
    print("O número é zero")
elif numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
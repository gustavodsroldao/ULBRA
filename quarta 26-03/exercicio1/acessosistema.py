# 1. Acesso ao sistema
# Peça ao usuário seu usuário e senha e verifique se o usuário é “admin” e a senha é “password” .
# Utilize uma estrutura condicional para informar em tela se o usuário pode acessar o sistema.
# Faça o fluxograma do algoritmo e depois o escreva em Python.

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
if usuario == "admin" and senha == "password":
    print("Acesso permitido")
else:
    print("Acesso negado")
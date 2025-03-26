# 1. Cálculo de Média 
# Peça ao usuário duas notas (float) e calcule a média. Exiba a média formatada em um número real.
# Utilize uma estrutura condicional para informar em tela se o aluno está aprovado, em recuperação ou reprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"A média das notas é: {media:.2f}")
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
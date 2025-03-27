# 4. Verificar se um aluno foi aprovado no trabalho
# Peça ao usuário a nota (deve tirar mais de 6 pontos) e a resposta “sim” ou “não” para os critérios:
# Entregou dentro do prazo?
# Apresentou o trabalho?
# Para facilitar: utilize o .strip().lower() == "sim” após o input
# Explicando:
# .strip() vai tirar qualquer símbolo de espaço da nossa resposta
# .lower() vai forçar todas letras serem em minúsculo (lembrem que python diferencia maiúsculo de minúsculo)
# == já vai fazer nosso relacional se a resposta foi sim e criar um booleano verdadeiro. 
# Qualquer outra resposta vai retornar como falso.
# Observação: Para realizar o envio crie um arquivo de texto (doc, txt), copie o enunciado do exercício e coloque sua resolução logo em seguida
# (do fluxograma pode ser o print, do código deve ser sua transcrição). Após todos os exercícios resolvidos, envie o arquivo pelo Aula.


nota = float(input("Digite a nota do aluno: "))
entrega = input("Entregou dentro do prazo? ").strip().lower() == "sim"
apresentacao = input("Apresentou o trabalho? ").strip().lower() == "sim"
if nota > 6 and entrega and apresentacao:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
# Desafio: Simulador de Estoque de Loja
# Contexto:
# Você foi contratado para desenvolver um programa simples que simula o controle de entrada e saída de produtos de uma loja durante um dia de funcionamento.
# Regras:
# - A loja começa com um estoque inicial de produtos (por exemplo, 100).
# - Durante o dia, o usuário pode escolher entre:
# 1: Vender um produto (subtrai do estoque)
# 2: Repor um produto (soma ao estoque)
# 3: Consultar estoque atual
# 4: Encerrar o expediente (encerra o loop)
# - O programa deve validar entradas (não pode vender se o estoque for 0).
# - Ao encerrar, o programa deve exibir quantas vendas e reposições foram feitas no dia.
# - O programa deve ser executado em um loop até que o usuário escolha encerrar o expediente.
# - Utilize estruturas de repetição e condicionais para implementar a lógica.


print ("Simulador de Estoque de Loja")
estoque = 25
vendas = 0
reposicoes = 0
while True:
    print(f"Estoque atual: {estoque}")
    print("Escolha uma opção:")
    print("1: Vender um produto")
    print("2: Repor um produto")
    print("3: Consultar estoque atual")
    print("4: Encerrar expediente")
    
    opcao = int(input("Digite sua opção (1-4): "))

    if opcao == 1:
        if estoque > 0:
            estoque -= 1
            vendas += 1
            print("Produto vendido! Estoque atual:", estoque)
        else:
            print("Não há produtos suficientes no estoque para vender.")
    elif opcao == 2:
        estoque += 1
        reposicoes += 1
        print("Produto reposto! Estoque atual:", estoque)
    elif opcao == 3:
        print("Estoque atual:", estoque)
    elif opcao == 4:
        print(f"Encerrando expediente... Vendas realizadas: {vendas}, Reposições realizadas: {reposicoes}")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")


estoque = 25
vendas = 0
reposicoes = 0

def venda(estoque, vendas, reposicoes):
    if estoque > 0:
        estoque -= 1
        vendas += 1
        print("Produto vendido! Estoque atual:", estoque)
    else:
        print("Não há produtos suficientes no estoque para vender.")
    return estoque, vendas, reposicoes

def reposicao(estoque, reposicoes):
    estoque += 1
    reposicoes += 1
    print("Produto reposto! Estoque atual:", estoque)
    return estoque, reposicoes

def consultar_estoque(estoque):
    if estoque > 0:
        print("Estoque atual:", estoque)
    else:
        print("Estoque vazio!")

def sair(estoque, vendas, reposicoes):
    print(f"Encerrando expediente... Vendas realizadas: {vendas}, Reposições realizadas: {reposicoes}")
    return False

def modo_venda(estoque, vendas, reposicoes):
    print("=== MODO DE VENDA ===")
    print("Digite 'sair' para voltar ao menu principal")    
    while True:
        acao = input("Digite 'vender' para vender um produto, 'repor' para repor um produto, ou 'sair' para encerrar o expediente: ")
        if acao.lower() == "sair":
            break
        elif acao.lower() == "vender":
            estoque, vendas, reposicoes = venda(estoque, vendas, reposicoes)
        else: 
            print("Opção inválida! Por favor, escolha uma opção entre 'vender', ou 'sair'.")
        
    return estoque, vendas, reposicoes

def modo_reposicao(estoque, reposicoes):
    print("=== MODO DE REPOSIÇÃO ===")
    print("Digite 'sair' para voltar ao menu principal")
    while True:
        acao = input("Digite 'repor' para repor um produto, 'consultar' para consultar o estoque ou 'sair' para encerrar o expediente: ")
        if acao.lower() == 'sair':
            break
        elif acao.lower() == 'repor':
            estoque, reposicoes = reposicao(estoque, reposicoes)
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 'repor', ou 'sair'.")
            
    return estoque, reposicoes



print ("Simulador de Estoque de Loja")
estoque = 25
vendas = 0
reposicoes = 0

while True:
    consultar_estoque(estoque)
    print("Escolha uma opção:")
    print("1: Vender um produto")
    print("2: Repor um produto")
    print("3: Consultar estoque atual")
    print("4: Encerrar expediente")

    opcao = input("Digite sua opção: ")
    if opcao == "1":
        estoque, vendas, reposicoes = modo_venda(estoque, vendas, reposicoes)
    elif opcao == "2":
        estoque, reposicoes = modo_reposicao(estoque, reposicoes)
    elif opcao == "3":
        consultar_estoque(estoque)
    elif opcao == "4":
        sair(estoque, vendas, reposicoes)
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")
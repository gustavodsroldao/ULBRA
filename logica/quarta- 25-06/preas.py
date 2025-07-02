# Criar um programa com funções compostas para gerenciar missões espaciais usando dicionários em Python. 
# Através de um menu interativo, será possível cadastrar missões, atualizar dados, consultar status, e gerar relatórios.
#
# Funcionalidades obrigatórias:
# 1. Cadastrar Nova Missão
#    - Solicita nome, destino, status inicial e se é tripulada.
#    - Verifica se já existe uma missão com o mesmo nome.
#
# 2. Atualizar Status da Missão
#    - Permite alterar o status da missão.
#    - Só altera se a missão existir.
#
# 3. Atualizar Destino da Missão
#    - Altera o destino da missão informada.
#
# 4. Marcar Missão como Tripulada/Não Tripulada
#    - Atualiza o campo tripulada.
#
# 5. Listar Todas as Missões
#    - Mostra nome, destino, status e se é tripulada, organizadamente.
#
# 6. Listar Missões por Status
#    - Permite ao usuário digitar um status e exibe apenas as missões correspondentes.
#
# 7. Remover Missão
#    - Apaga uma missão do dicionário, se existir.
#
# 8. Verificar Existência de Missão
#    - Informa se determinada missão está cadastrada.
#
# 9. Contar Missões por Tipo (Tripulada ou Não)
#    - Exibe o total de missões tripuladas e não tripuladas.
#
# 10. Limpar Todas as Missões
#     - Após confirmação do usuário, apaga todos os registros com .clear().
#
# 11. Sair do Programa
#
# Requisitos Técnicos:
# - Cada item do menu deve ser implementado com uma função separada.
# - Usar parâmetros e retornos para o compartilhamento e modificação do dicionário.
# - O programa principal deve conter um loop com menu, chamando cada função conforme a opção escolhida.
#
# Desafio EXTRA:
# - Criar uma função para gerar um "relatório" com percentual de missões concluídas.
# - Adicionar um campo "ano_lancamento" e permitir filtrar por ano.

missoes = {}

def cadastrar_nova_missao(missoes):
    nome_missao = input("Digite o nome da missão: ")

    if nome_missao in missoes:
        print("Erro: Já existe uma missão com este nome!")
        return missoes
    
    destino_missao = input("Digite o destino da missão: ")
    ano_lancamento = input("Digite o ano de lançamento da missão: ")
    if not ano_lancamento.isdigit():
        print("Ano inválido! Por favor, insira um ano válido.")
        return missoes
    status_inicial_missao = input("Digite o status inicial da missão: ")

    missao_tripulada = input("Esta missão é tripulada? (s/n): ").lower()

    # Neste caso, faz uma comparação de string, e retorna um booleano
    missao_is_tripulada = missao_tripulada == 's'

    missoes[nome_missao] = {
        'destino_missao': destino_missao,
        'status_inicial_missao': status_inicial_missao,
        'missao_is_tripulada': missao_is_tripulada,
        'ano_lancamento': ano_lancamento
    }

    print(f"Missão, cujo nome é {nome_missao}, foi cadastrada com sucesso!")

    return missoes


def atualizar_status_missao(missoes):
    nome_missao = input("Digite o nome da missão: ")

    if nome_missao in missoes:
        status_missao = input("Digite o novo status da missão: ")
        missoes[nome_missao]['status_inicial_missao'] = status_missao

        print(f"Antigo status da missão {nome_missao}, era {missoes[nome_missao]['status_inicial_missao']}, e a partir deste momento, passou para {status_missao}!")
    else:
        print("Erro: Missão não encontrada!")

    return missoes

def atualizar_destino_missao(missoes):
    nome_missao = input("Digite o nome da missão: ")

    if nome_missao in missoes:
        destino_missao = input("Digite o novo destino da missão: ")
        missoes[nome_missao]['destino_missao'] = destino_missao
        print(f"Destino da missão {nome_missao} atualizado para {destino_missao}!")
    else:
        print("Erro: Missão não encontrada!")

    return missoes

def atualizar_tripulacao_missao():
    nome_missao = input("Digite o nome da missão: ")

    if nome_missao in missoes:
        missaoIsTripulada = input("Esta missão é tripulada? (s/n): ").lower()

        # Neste caso, faz uma comparação de string, e retorna um booleano
        missaoIsTripulada = missaoIsTripulada == 's'

        missoes[nome_missao]['missaoIsTripulada'] = missaoIsTripulada
        status = "tripulada" if missaoIsTripulada else "não tripulada"

        print(f"Missão cujo nome é {nome_missao}, agora é {status}!")
    else:
        print("Erro: Missão não encontrada!")

    return missoes

def listar_todas_missoes(missoes):
    if not missoes:
        print("Não há missões cadastradas!")
        return
    
    print("\n" + "="*30)
    print("Lista de todas as missões:")
    print("="*30 + "\n")

    for nome_missao, dados_missao in missoes.items():
        status_missao = "Tripulada" if dados_missao['missaoIsTripulada'] else "Não Tripulada"
        print(f"Nome da missao: {nome_missao}")
        print(f"Destino da missão: {dados_missao['destino_missao']}")
        print(f"Status da missão: {dados_missao['status_inicial_missao']}")
        print(f"Tripulada: {status_missao}")
        print("-"*30)

    print("\n" + "="*30)

    return missoes

def listar_todas_missoes_por_status(missoes, status):
    if not missoes:
        print("Não há missões cadastradas!")
        return
    
    missoes_filtradas = {nome: dados for nome, dados in missoes.items() if dados['status_inicial_missao'].lower() == status.lower()}
    print(f"\nListando missões com status: {status}")
    print("="*30 + "\n")
    if not missoes_filtradas:
        print(f"Nenhuma missão encontrada com o status: {status}")
    else:
        for nome_missao, dados_missao in missoes_filtradas.items():
            status_missao = "Tripulada" if dados_missao['missaoIsTripulada'] else "Não Tripulada"
            print(f"Nome da missão: {nome_missao}")
            print(f"Destino da missão: {dados_missao['destino_missao']}")
            print(f"Status da missão: {dados_missao['status_inicial_missao']}")
            print(f"Tripulada: {status_missao}")
            print("-"*30)


def remover_missao(missoes):
    nome_missao = input("Digite o nome da missão: ")

    if nome_missao in missoes:
        confirmarRemocao = input("Tem certeza que deseja remover a missão? (s/n): ").lower()

        # Neste caso, faz uma comparação de string, e retorna um booleano
        confirmadaRemocao = confirmarRemocao == 's'

        if confirmadaRemocao:
            del missoes[nome_missao]
            print(f"Missão cujo nome é {nome_missao}, foi removida com sucesso do planejamento!")
        else:
            print("Remoção cancelada!")
    else:
        print("Erro: Missão não encontrada!")

def concluir_missao(missoes):
    print("OBS:  Use a palavra 'concluida' para marcar a missão como concluída!")
    nome_missao = input("Digite o nome da missão :")
    if nome_missao in missoes:
        missoes[nome_missao]['status_inicial_missao'] = 'concluida'
        print(f"Missão {nome_missao} marcada como concluída!")
    else:
        print("Erro: Missão não encontrada!")


def verificar_existencia_missao(missoes):
    nome_missao = input("Digite o nome da missão: ")

    if nome_missao in missoes:
        print("\n" + "="*30)

        print(f"Missão cujo nome é {nome_missao}, está cadastrada no nosso CRM AUSTRONAUTICO!")

        dados_missao = missoes[nome_missao]
        missao_tripulada = "Tripulada" if dados_missao['missaoIsTripulada'] else "Não Tripulada"
        
        print(f"Destino da missão: {dados_missao['destino_missao']}")
        print(f"Status da missão: {dados_missao['status_inicial_missao']}")
        print(f"Missão tripulada: {missao_tripulada}")

        print("\n" + "="*30)
    else:
        print(f"Missão cujo nome é {nome_missao}, não está cadastrada no nosso CRM AUSTRONAUTICO!")
    
def classificar_tipo_missao(missoes):
    missoes_tripuladas = 0
    missoes_não_tripuladas = 0

    for dados_missao in missoes.values():
        if dados_missao['missaoIsTripulada']:
            tripuladas += 1
        else:
            missoes_não_tripuladas += 1

    total = len(missoes)

    print("\n" + "="*30 )
    print("Contagem de missões cadastradas no CRM AUSTRONAUTICO:")
    print("\n" + "="*30 )
    print(f"Total de missões triupaladas: {missoes_tripuladas}")
    print(f"Total de missões não tripuladas: {missoes_não_tripuladas}")
    print(f"Total de missoes: {total}")

def excluir_todas_missoes(missoes):
    confirmarExclusao = input("Tem certeza que deseja excluir todas as missões cadastradas no CRM AUSTRONAUTICO? (s/n): ").lower()
    
     # Neste caso, faz uma comparação de string, e retorna um booleano
    exclusaoConfirmada = confirmarExclusao == 's'

    if exclusaoConfirmada == 's':
        missoes.clear()
        print("Todas as missões foram excluídas com sucesso!")
    else:
        print("Exclusão cancelada!")

    return missoes

def sair_do_crm_austronautico():
    print("Saindo do CRM AUSTRONAUTICO...")
    print("Obrigado por usar o CRM AUSTRONAUTICO!")
    print("Até a próxima!")
    exit()

def relatorio(missoes):
    if not missoes:
        print("Não há missões cadastradas para gerar relatório!")
        return
    
    total_missoes = len(missoes)
    if total_missoes == 0:
        print("Não há missões cadastradas para gerar relatório!")
        return
    
    missoes_concluidas = sum(1 for dados_missao in missoes.values() if dados_missao['status_inicial_missao'].lower() == 'concluida')
    print("\n" + "="*30)
    print("Relatório de Missões Espaciais")
    print (f"Total de missões concluídas: {missoes_concluidas} de {total_missoes}")
    print(f"Percentual de missões concluídas: {missoes_concluidas / total_missoes * 100:.2f}%")
    print("\n" + "="*30)

def listar_missoes_por_ano(missoes):
    if not missoes:
        print("Não há missões cadastradas!")
        return
    
    ano = input("Digite o ano para filtrar as missões: ")

    if not ano.isdigit():
        print("Ano inválido! Por favor, insira um ano válido.")
        return
    
    missoes_filtradas = {
        nome: dados for nome, dados in missoes.items() if dados['ano_lancamento'] == ano
    }

    if not missoes_filtradas:
        print(f"Nenhuma missão encontrada para o ano {ano}.")
        return
    
    print(f"\nListando missões do ano {ano}:")
    print(f"Missão(s) encontradas: {len(missoes_filtradas)}")
    print("="*30 + "\n")

def menu():
    while True: 
        print("CRM AUSTRONAUTICO - Missões Espaciais")
        print("="*30)
        print("1. Cadastrar Nova Missão")
        print("2. Atualizar Status da Missão")
        print("3. Atualizar Destino da Missão")
        print("4. Marcar Missão como Tripulada/Não Tripulada")
        print("5. Listar Todas as Missões")
        print("6. Listar Missões por Status")
        print("7. Remover Missão")
        print("8. Concluir missão")
        print("9. Verificar Existência de Missão")
        print("10. Contar Missões por Tipo (Tripulada ou Não)")
        print("11. Listar missões por ano")
        print("12. Limpar Todas as Missões")
        print("13. Gerar Relatório de Missões Concluídas")
        print("14. Sair do Programa")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_nova_missao(missoes)
        elif opcao == '2':
            atualizar_status_missao(missoes)
        elif opcao == '3':
            atualizar_destino_missao(missoes)
        elif opcao == '4':
            atualizar_tripulacao_missao()
        elif opcao == '5':
            listar_todas_missoes(missoes)
        elif opcao == '6':
            status = input("Digite o status para filtrar as missões: ")
            listar_todas_missoes_por_status(missoes, status)
        elif opcao == '7':
            remover_missao(missoes)
        elif opcao == '8':
            concluir_missao(missoes)
        elif opcao == '9':
            verificar_existencia_missao(missoes)
        elif opcao == '10':
            classificar_tipo_missao(missoes)
        elif opcao == '11':
            listar_missoes_por_ano(missoes)
        elif opcao == '12':
            excluir_todas_missoes(missoes)
        elif opcao == '13':
            relatorio(missoes)
        elif opcao == '14':
            sair_do_crm_austronautico()
        else:
            print("Opção inválida! Tente novamente.")

menu()
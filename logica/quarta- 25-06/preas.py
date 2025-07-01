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
    status_inicial_missao = input("Digite o status inicial da missão: ")

    missao_tripulada = input("Esta missão é tripulada? (s/n): ").lower()

    # Neste caso, faz uma comparação de string, e retorna um booleano
    missaoIsTripulada = missao_tripulada == 's'

    missoes[nome_missao] = {
        'destino_missao': destino_missao,
        'status_inicial_missao': status_inicial_missao,
        'missaoIsTripulada': missaoIsTripulada
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
import json
import os

especies = {}
tutores = {}

# Função para carregar dados do arquivo JSON
def carregar_dados():
    global especies, tutores
    
    # Verificar se o arquivo existe
    if os.path.exists('animais.json'):
        try:
            with open('animais.json', 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                especies = dados.get('especies', {})
                tutores = dados.get('tutores', {})
            print("Dados carregados com sucesso!")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            especies = {}
            tutores = {}
    else:
        print("Arquivo de dados não encontrado. Iniciando com dados vazios.")
        especies = {}
        tutores = {}

# Função para salvar dados no arquivo JSON
def salvar_dados():
    try:
        dados = {
            'especies': especies,
            'tutores': tutores
        }
        
        with open('animais.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

# 1. Cadastrar Animais:
# Nome da espécie
# Tipo (domesticável ou selvagem)
# Nível de periculosidade (1 a 5)

def cadastrar_especie(especies):
    nome_especie = input("Digite o nome da espécie que deseja cadastrar: ")

    # Validação 1: Verificar se a espécie já existe
    if nome_especie in especies:
        print("Erro: Já existe uma espécie com este nome!")
        return especies

    # Validação 2: Verificar se o nome da espécie contém apenas letras
    if not nome_especie.isalpha():
        print("Erro: Nome da espécie deve conter apenas letras!")
        return especies

    # Validação 3: Verificar se o tipo da espécie é válido
    tipo_especie = input("Digite o tipo da espécie (Domesticável ou Selvagem): ").lower()

    if tipo_especie not in ["domesticável", "selvagem"]:
        print("Erro: Tipo de espécie inválido!")
        return especies
    
    # Validação 4: Verificar se o nível de periculosidade é um número entre 1 e 5
    nivel_periculosidade = int(input("De 1 a 5, digite o nível de periculosidade da espécie: "))

    if nivel_periculosidade < 1 or nivel_periculosidade > 5:
        print("Erro: Nível de periculosidade deve ser um número entre 1 e 5!")
        return especies

    especies[nome_especie] = {
        "tipo": tipo_especie,
        "nivel_periculosidade": nivel_periculosidade
    }

    print(f"Espécie {nome_especie} cadastrada com sucesso, de {tipo_especie} e nível de periculosidade {nivel_periculosidade}")
    
    # Salvar dados após cadastro
    salvar_dados()
    return especies


# Cadastrar Tutores:
# Nome completo
# CPF (apenas validação de quantidade de dígitos — 11)

def cadastrar_tutor(tutores):
    nome_tutor = input("Digite o nome do tutor que deseja cadastrar: ")
    cpf_tutor = input("Digite o CPF do tutor: ")

    # Validação 1: Verificar se o nome do tutor já existe
    if nome_tutor in tutores:
        print("Erro: Já existe um tutor com este nome!")
        return tutores

    # Validação 2: Verificar se o CPF tem 11 dígitos
    if len(cpf_tutor) != 11:
        print("Erro: CPF deve ter 11 dígitos!")
        return tutores

    # Validação 3: Verificar se o CPF contém apenas números
    if not cpf_tutor.isdigit():
        print("Erro: CPF deve conter apenas números!")
        return tutores
    
    # Cadastrar o tutor
    tutores[nome_tutor] = {
        "cpf": cpf_tutor,
        "animais": []
    }

    print(f"Tutor com CPF {cpf_tutor} e nome {nome_tutor} cadastrado com sucesso!")
    
    # Salvar dados após cadastro
    salvar_dados()
    return tutores

# 3. Atribuir Animal a Tutor:
# Regras:
# Apenas animais domesticáveis podem ter tutores.
# Um tutor pode ter no máximo 3 animais.
# Um animal pode ter múltiplos tutores (desde que seja domesticável).

def atribuir_animal_a_tutor(tutores):
    nome_animal = input("Digite o nome do animal que deseja atribuir a um tutor: ")
    nome_tutor = input("Digite o nome do tutor que deseja atribuir o animal: ")

    # Validação 1: Verificar se o animal existe
    if nome_animal not in especies:
        print("Erro: Animal e espécie não encontrados!")
        return tutores

    # Validação 2: Verificar se o tutor existe
    if nome_tutor not in tutores:
        print("Erro: Tutor não encontrado!")
        return tutores

    # Validação 3: Verificar se o animal é domesticável
    if especies[nome_animal]["tipo"] == "selvagem":
        print("Erro: Animal não é domesticável!")
        return tutores

    # Validação 4: Verificar se o tutor já tem 3 animais
    if len(tutores[nome_tutor]["animais"]) >= 3:
        print("Erro: Tutor já tem 3 animais!")
        return tutores

    # Se todas as validações passaram, atribuir o animal ao tutor
    tutores[nome_tutor]["animais"].append(nome_animal)
    print(f"Animal {nome_animal} atribuído ao tutor {nome_tutor} com sucesso!")
    
    # Salvar dados após atribuição
    salvar_dados()
    return tutores

def listar_animais_por_filtro(tutores, especies):
    print("1. Listar todos os animais cadastrados com tutores")
    print("2. Listar todos os animais cadastrados sem tutores")
    
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("\n=== ANIMAIS COM TUTORES ===")
        for nome_tutor, informacao_tutor in tutores.items():
            if informacao_tutor['animais']:  # Só mostra se tem animais
                print(f"\nTutor: {nome_tutor}")
                print(f"CPF: {informacao_tutor['cpf']}")
                print(f"Animais: {', '.join(informacao_tutor['animais'])}")
            else:
                print(f"\nTutor: {nome_tutor} - Nenhum animal atribuído")

    elif opcao == "2":
        print("\n=== ANIMAIS SEM TUTORES ===")
        
        # Coletar todos os animais que têm tutores
        animais_com_tutor = []
        for tutor_info in tutores.values():
            animais_com_tutor.extend(tutor_info['animais'])
        
        # Mostrar animais individuais que não têm tutores
        animais_sem_tutor = []
        for animal in especies.keys():
            if animal not in animais_com_tutor:
                animais_sem_tutor.append(animal)
        
        if animais_sem_tutor:
            print("Animais individuais sem tutores:")
            for animal in animais_sem_tutor:
                print(f"\nAnimal: {animal}")
                print(f"Tipo: {especies[animal]['tipo']}")
                print(f"Nível de Periculosidade: {especies[animal]['nivel_periculosidade']}")
        else:
            print("Todos os animais cadastrados têm tutores!")
            
    else:
        print("Opção inválida!")
        
    return tutores, especies

def listar_tutores_e_animais_atribuidos(tutores, especies):
    print("\n=== TUTORES E ANIMAIS ATRIBUÍDOS ===")
    for nome_tutor, informacao_tutor in tutores.items():
        print(f"\nTutor: {nome_tutor}")
        print(f"CPF: {informacao_tutor['cpf']}")
        print(f"Animais atribuídos: {', '.join(informacao_tutor['animais'])}")
    return tutores, especies

def remover_animal_de_tutor(tutores):
    nome_tutor = input("Digite o nome do tutor que deseja remover o animal: ")
    nome_animal = input("Digite o nome do animal que deseja remover: ")

    # Validação 1: Verificar se o tutor existe
    if nome_tutor not in tutores:
        print("Erro: Tutor não encontrado!")
        return tutores
    
    # Validação 2: Verificar se o animal existe
    if nome_animal not in especies:
        print("Erro: Animal não encontrado!")
        return tutores
    
    # Validação 3: Verificar se o animal está atribuído ao tutor
    if nome_animal not in tutores[nome_tutor]["animais"]:
        print("Erro: Animal não atribuído ao tutor!")
        return tutores
    
    # Remover o animal do tutor
    tutores[nome_tutor]["animais"].remove(nome_animal)
    print(f"Animal {nome_animal} removido do tutor {nome_tutor} com sucesso!")

    # Salvar dados após remoção
    salvar_dados()
    return tutores

# Função principal do programa
def main():
    global especies, tutores
    
    # Carregar dados ao iniciar
    carregar_dados()
    
    while True:
        print("\n" + "="*50)
        print("PET SYSTEM")
        print("="*50)
        print("1. Cadastrar espécie")
        print("2. Cadastrar tutor")
        print("3. Atribuir animal a tutor")
        print("4. Remover animal de tutor")
        print("5. Listar animais por filtro")
        print("6. Listar tutores")
        print("7. Salvar dados")
        print("8. Sair")
        print("="*50)
        
        opcao = input("Digite sua opção: ")
        
        if opcao == "1":
            cadastrar_especie(especies)
        elif opcao == "2":
            cadastrar_tutor(tutores)
        elif opcao == "3":
            atribuir_animal_a_tutor(tutores)
        elif opcao == "4":
            remover_animal_de_tutor(tutores)
        elif opcao == "5":
            listar_animais_por_filtro(tutores, especies)
        elif opcao == "6":
            listar_tutores_e_animais_atribuidos(tutores, especies)
        elif opcao == "7":
            salvar_dados()
        elif opcao == "8":
            print("Salvando dados antes de sair...")
            salvar_dados()
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida!")

# Executar o programa se este arquivo for executado diretamente
if __name__ == "__main__":
    main()
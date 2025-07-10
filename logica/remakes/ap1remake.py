#  Recrie o algoritmo entregue na AP1 utilizando uma função com estrutura de repetição
#  para validar a entrada dos valores das respostas de 1 a 5.


def perguntas():
    print("Com base nas perguntas abaixo, escolha a área que mais combina com você. \nResponda de 1 a 5, onde 1 é 'Discordo totalmente' e 5 é 'Concordo totalmente'.")
    

    perguntas_desenvolvedor = [
        "Gosto de programar e resolver problemas com código.",
        "Tenho interesse em criar aplicativos e sites.",
        "Gosto de aprender novas linguagens de programação.",
        "Prefiro trabalhar com lógica e estruturação de código.",
        "Tenho paciência para depurar erros e otimizar código.",
    ]

    perguntas_tester = [
        "Gosto de testar e garantir que sistemas funcionem corretamente.",
        "Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos.",
        "Acredito que testes automatizados ajudam a evitar falhas em sistemas.",
        "Gosto de seguir padrões e documentar processos para garantir qualidade.",
        "Quero trabalhar garantindo que um software funcione bem para todos os usuários.",
    ]

    perguntas_uxdesigner = [
        "Gosto de pensar na experiência do usuário ao usar um sistema.",
        "Tenho interesse em pesquisa de mercado e comportamento do usuário.",
        "Me interesso por criar soluções inovadoras e intuitivas.",
        "Gosto de trabalhar com design, wireframes ou prototipagem.",
        "Quero entender e definir estratégias para melhorar produtos digitais.",
    ]

    # faz a coleta das respostas
    respostas_desenvolvedor = []
    respostas_tester = []
    respostas_uxdesigner = []

    for pergunta in perguntas_desenvolvedor:
        resposta = validar_resposta(pergunta)
        respostas_desenvolvedor.append(resposta)
    
    for pergunta in perguntas_tester:
        resposta = validar_resposta(pergunta)
        respostas_tester.append(resposta)
    
    for pergunta in perguntas_uxdesigner:
        resposta = validar_resposta(pergunta)
        respostas_uxdesigner.append(resposta)

    return {
        "respostas_desenvolvedor": respostas_desenvolvedor,
        "respostas_tester": respostas_tester,
        "respostas_uxdesigner": respostas_uxdesigner,
    }


def calcular_pontuacao(respostas_desenvolvedor, respostas_tester, respostas_uxdesigner):
    soma_respostas_desenvolvedor = sum(respostas_desenvolvedor)    
    soma_respostas_tester = sum(respostas_tester)    
    soma_respostas_uxdesigner = sum(respostas_uxdesigner)    
    
    media_desenvolvedor = soma_respostas_desenvolvedor / len(respostas_desenvolvedor)
    media_tester = soma_respostas_tester / len(respostas_tester)
    media_uxdesigner = soma_respostas_uxdesigner / len(respostas_uxdesigner)

    print(f"Média das respostas do desenvolvedor: {media_desenvolvedor:.0f}")
    print(f"Média das respostas do tester: {media_tester:.0f}")
    print(f"Média das respostas do uxdesigner: {media_uxdesigner:.0f}")

    if media_desenvolvedor > media_tester and media_desenvolvedor > media_uxdesigner:
        print("Você tem maior afinidade com a área de desenvolvimento de software.")
    elif media_tester > media_desenvolvedor and media_tester > media_uxdesigner:
        print("Você tem maior afinidade com a área de teste de software.")
    else:
        print("Você tem maior afinidade com a área de design de experiência do usuário.")


def validar_resposta(pergunta):
    while True: # Vai ser executado até que a resposta seja válida
        try:
            resposta = int(input(pergunta + "\n"))
            if 1 <= resposta <= 5:
                return resposta # Sai do loop se for válido
            else:
                print("Resposta inválida. Por favor, responda com um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")


def main():
    print("Bem-vindo ao teste de aptidão para desenvolvimento de software.")

    resultado = perguntas()

    calcular_pontuacao(resultado["respostas_desenvolvedor"], resultado["respostas_tester"], resultado["respostas_uxdesigner"])

if __name__ == "__main__":
    main()
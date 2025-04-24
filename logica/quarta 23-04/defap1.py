# Regras:
# O jogo terá 3 áreas de interesse:

# a. Desenvolvimento de Software
# b. Área de Produtos (UX/UI, Product Owner, Product Manager, etc.)
# c. Área de Qualidade (Testes, QA, automação de testes, etc.)

# Para cada área, serão feitas 5 perguntas.
# As respostas devem ser um número de 1 a 5 (onde 1 é "Discordo totalmente" e 5 é "Concordo totalmente").
# No final, o algoritmo soma os pontos de cada área e determina qual é a área de maior afinidade.
# Se houver empate entre duas ou mais áreas, o algoritmo retorna todas as áreas empatadas
# O jogo deve ser escrito em um algoritmo utilizando python e fluxograma.

# Para as perguntas de desenvolvimento de software, utilize: 

# Gosto de programar e resolver problemas com código.
# Tenho interesse em criar aplicativos e sites.
# Gosto de aprender novas linguagens de programação.
# Prefiro trabalhar com lógica e estruturação de código.
# Tenho paciência para depurar erros e otimizar código.
# Para as perguntas da área de produto, utilize:

# Gosto de pensar na experiência do usuário ao usar um sistema.
# Tenho interesse em pesquisa de mercado e comportamento do usuário.
# Me interesso por criar soluções inovadoras e intuitivas.
# Gosto de trabalhar com design, wireframes ou prototipagem.
# Quero entender e definir estratégias para melhorar produtos digitais.
# Para as perguntas da área de qualidade, utilize:

# Gosto de testar e garantir que sistemas funcionem corretamente.
# Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos.
# Acredito que testes automatizados ajudam a evitar falhas em sistemas.
# Gosto de seguir padrões e documentar processos para garantir qualidade.
# Quero trabalhar garantindo que um software funcione bem para todos os usuários.

# No final, o algoritmo soma os pontos de cada área e determina qual é a área de maior afinidade.
# Se houver empate entre duas ou mais áreas, o algoritmo retorna todas as áreas empatadas
# O jogo deve ser escrito em um algoritmo utilizando python e fluxograma.

# Agora usando uma função para validar a entrada do usuário

def validador(numero):
    while True:
        try:
            numero = int(input(numero))
            if 1 <= numero <=5:
                return numero
            else: 
                print("Número inválido. Digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 5.")

introducao = print("Com base nas perguntas abaixo, escolha a área que mais combina com você. Responda de 1 a 5, onde 1 é 'Discordo totalmente' e 5 é 'Concordo totalmente'.\n\n")

a1 = validador("Gosto de programar e resolver problemas com código.\n")
a2 = validador("Tenho interesse em criar aplicativos e sites.\n")
a3 = validador("Gosto de aprender novas linguagens de programação.\n")
a4 = validador("Prefiro trabalhar com lógica e estruturação de código.\n")
a5 = validador("Tenho paciência para depurar erros e otimizar código.\n")

b1 = validador("Gosto de pensar na experiência do usuário ao usar um sistema.\n")
b2 = validador("Tenho interesse em pesquisa de mercado e comportamento do usuário.\n")
b3 = validador("Me interesso por criar soluções inovadoras e intuitivas.\n")
b4 = validador("Gosto de trabalhar com design, wireframes ou prototipagem.\n")
b5 = validador("Quero entender e definir estratégias para melhorar produtos digitais.\n")

c1 = validador("Gosto de testar e garantir que sistemas funcionem corretamente.\n")
c2 = validador("Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos.\n")
c3 = validador("Acredito que testes automatizados ajudam a evitar falhas em sistemas.\n")
c4 = validador("Gosto de seguir padrões e documentar processos para garantir qualidade.\n")
c5 = validador("Quero trabalhar garantindo que um software funcione bem para todos os usuários.\n")

soma_a = a1 + a2 + a3 + a4 + a5
soma_b = b1 + b2 + b3 + b4 + b5
soma_c = c1 + c2 + c3 + c4 + c5

if soma_a > soma_b and soma_a > soma_c:
    print("Você tem maior afinidade com a área de Desenvolvimento de Software.")
elif soma_b > soma_a and soma_b > soma_c:
    print("Você tem maior afinidade com a área de Produtos.")
elif soma_c > soma_a and soma_c > soma_b:
    print("Você tem maior afinidade com a área de Qualidade.")
elif soma_a == soma_b and soma_a > soma_c:
    print("Você tem afinidade com as áreas de Desenvolvimento de Software e Produtos.")
elif soma_a == soma_c and soma_a > soma_b:
    print("Você tem afinidade com as áreas de Desenvolvimento de Software e Qualidade.")
elif soma_b == soma_c and soma_b > soma_a:
    print("Você tem afinidade com as áreas de Produtos e Qualidade.")
else:
    print("Você tem afinidade com as áreas de Desenvolvimento de Software, Produtos e Qualidade.")
numero = int(input("Digite um número de 4 dígitos: "))

if 1000 <= numero <= 9999:
    milhar = numero // 1000
    centena = (numero // 100) % 10
    dezena = (numero // 10) % 10
    unidade = numero % 10
    
    palindromo = (milhar - unidade == 0) * (centena - dezena == 0)
    repetidos = (milhar == centena) + (milhar == dezena) + (milhar == unidade) + (centena == dezena) + (centena == unidade) + (dezena == unidade)
    soma = milhar + centena + dezena + unidade
    
    # Determinar maior dígito e posição
    maior = milhar
    posicao = 1
    
    if centena > maior:
        maior = centena
        posicao = 2 
    if dezena > maior:
        maior = dezena
        posicao = 3
    if unidade > maior:
        maior = unidade
        posicao = 4
    
    print(f"Milhar: {milhar}")
    print(f"Centena: {centena}")
    print(f"Dezena: {dezena}")
    print(f"Unidade: {unidade}")
    print(f"Soma dos dígitos: {soma}")
    print(f"Maior dígito: {maior} (Posição: {posicao})")             
    print(f"Palíndromo: {'Sim' if palindromo else 'Não'}")
    print(f"Repetidos: {'Sim' if repetidos > 0 else 'Não'}")
else:
    print("Número inválido. O número deve ter 4 dígitos.")

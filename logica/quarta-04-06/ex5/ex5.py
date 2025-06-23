# Validador de senha
# Descrição: Crie uma função validar_senha(senha) que verifica se a senha:
# Possui ao menos 8 caracteres
# Contém ao menos uma letra e um número (utilize "caractere.isalpha()" para verificar se possui letras e "caractere.isdigit()" para verificar se tem números)
# Use estruturas condicionais e percorra a string com for. Retorne "Senha válida" ou "Senha inválida".

def validar_senha(senha):
    tem_letra = False
    tem_numero = False
    
    if len(senha) >= 8:
        for caractere in senha:
            if caractere.isalpha():
                tem_letra = True
            if caractere.isdigit():
                tem_numero = True
        
        if tem_letra and tem_numero:
            return "Senha válida"
        else:
            return "Senha inválida"
    else:
        return "Senha inválida"

senha = input("Digite a senha: ")
print(validar_senha(senha))
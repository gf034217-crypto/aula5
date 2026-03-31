def validarSenha(senha):
    if len(senha) <8:
        return 'Senha invalida, muito curta'
    temNumero = False
    temMaiuscula = False

    for c in senha:
        if c == ' ':
            return 'Senha inavalida, não pode conter espaços'
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c<= 'Z':
            temMaiuscula = True
        
    if not temNumero:
        return 'senha inavalida não tem numero.'
    if not temMaiuscula:
        return 'senha invalida não tem Maiuscula'
    
    return 'Senha valida'
#main
senha = input('Digite sua senha:')
print(validarSenha(senha))
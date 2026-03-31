def calcular_media(prod, qual, pont):
    return(prod + qual + pont) / 3
def classificar(media):
    if media >= 8:
        return 'excelente'
    elif media >= 6:
        return 'bom'
    else:
        return 'critico'
def avaliarFuncionarios():
    total = 0
    exc = 0
    bom = 0
    crit = 0
    melhorNome = ''
    melhorMedia = -1
    while True:
        nome = input('nome do funcionario:')
        if nome == 'fim':
            break
    prod = float(input('produtividade:'))
    qual = float(input('qualidade:'))
    pont = float(input('pontualiade:'))

    media = calcular_media(prod,qual,pont)
    categoria = classificar(media)
    print (f'{nome}, media {media}, {categoria}')

    total += 1
    if categoria == 'Excelente':
        exc += 1
    elif categoria == 'bom':
        bom += 1
    else:
        crit += 1

    if media > melhorMedia:
        melhorMedia = media
        melhorNome = nome

    if total == 0:
        print('nada para calcular')
        return
    print('-' * 50)
    print("relatorio")
    print('-' * 50)
    print(f'total de func {total}:')
    print(f'excelente {exc}')
    print(f'bom {bom}')
    print(f'critico {crit}')
    print(f"melhor func: {melhorNome}")
    print(f'melhor media{melhorMedia}')

avaliarFuncionarios()
    
def ehprimo(n):
    if n > 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
valor = int(input('N='))
if ehprimo(valor):
    print('PRIMO')
else:
    print('Não é primo')

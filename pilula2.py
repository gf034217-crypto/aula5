def simulaCrescimento(populacao, taxa, limite):
    anos = 0
    while populacao < limite:
        populacao = populacao * (1+ taxa)
        anos += 1
    return anos

#main 
p = float(input('população inicia'))
t = float(input('taxa (%):'))/100
l = float(input('Limite:'))

print(f'Anos = {simulaCrescimento(p,t,l)}')

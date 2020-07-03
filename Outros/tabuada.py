'''
    Programa que mostra a tabuada do numero escolhido
    pelo usuario
'''
n = int(input('Informe o numero para saber a sua tabuada:  '))
for c in range(0, 11):
    resp = n * c
    print(f'{n} x {c} = {resp}')
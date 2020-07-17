valor = float(input())
notas = (100, 50, 20, 10, 5, 2)
moedas = (1.0, 0.50, 0.25, 0.10, 0.05, 0.01)
print('NOTAS:')
for n in notas:
    total = valor // n
    print('{:.0f} nota (s) de R$ {:.0f}'.format(total, n))
    valor -= total * n
print('MOEDAS:')
total = 0
for m in moedas:
    total = valor // m
    print('{} moeda(s) de R$ {}'.format(total, m))
    valor -= total * m
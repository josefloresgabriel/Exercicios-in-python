valor = float(input())
notas = (100, 50, 20, 10, 5, 2)
moedas = (1.0, 0.50, 0.25, 0.10, 0.05, 0.01)
print('NOTAS:')
for n in notas:
    total = int(valor / n)
    print('{:.0f} nota (s) de R$ {:.2f}'.format(total, n))
    valor -= total * n

print('MOEDAS:')
for m in moedas:
    totalmoedas = int(valor / m)
    print('{:.0f} moeda(s) de R$ {:.2f}'.format(totalmoedas, m))
    valor -= totalmoedas * m
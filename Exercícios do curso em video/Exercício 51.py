a1 = int(input('Informe o primeiro número de uma P.A: '))
r = int(input('Informe a razão dessa P.A: '))
f = a1 + (10 - 1) * r
for p in range(a1, f, r):
    print(p, end= ' ')

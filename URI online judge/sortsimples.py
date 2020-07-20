valores = str(input()).split()
v1 = float(valores[0])
v2 = float(valores[1])
v3 = float(valores[2])
desordenado = [v1, v2, v3]
ordenado = sorted(desordenado)
for valor in ordenado:
    print('{:.0f}'.format(valor))
print('')
for valor in desordenado:
    print('{:.0f}'.format(valor))
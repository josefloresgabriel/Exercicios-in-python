coordenadas = str(input()).split()
x = float(coordenadas[0])
y = float(coordenadas[1])
if x == 0 and y == 0:
    print('Origem')
elif x > 0 and y > 0:
    print('Q1')
elif x > 0 and y < 0:
    print('Q4')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x == 0 and y != 0:
    print('Eixo Y')
else:
    print('Eixo X')
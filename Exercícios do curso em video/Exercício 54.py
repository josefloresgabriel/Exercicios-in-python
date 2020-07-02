from datetime import datetime
p = datetime.today().year
cont2 = 0
cont3 = 0
for contador in range(1, 8):
    a = int(input(f'Em que ano a {contador} pessoa nasceu? '))
    idade = p - a
    if idade >= 18:
        cont2 += 1
    else:
        cont3 += 1
print(f'Analisando as setes pessoas, sabemos que {cont2} são maiores de idade e {cont3} são menores de idade.')
total = 0
n = int(input('Informe um número inteiro: '))
for c in range(1, n +1):
    if n % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[36m', end=' ')
print(f'{c}', end=' ')
if total >= 3:
    print(f'\n\033[35mO número {n} não é primo.')
elif total == 2:
    print(f'\n\033[35mO número {n} é primo.')


s = 0
for n in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s += n
print(f'A soma entre eles é {s}')
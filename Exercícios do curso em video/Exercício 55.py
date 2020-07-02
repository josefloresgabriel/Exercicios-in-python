ma = 0
me = 0
for c in range(1, 6):
    p = float(input(f'Digite o peso da {c} pessoa: '))
    if c == 1:
        ma = p
        me = p
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print(f'\033[34mO maior peso foi {ma}Kg', end=' ')
print(f'e o menor peso foi {me}Kg')
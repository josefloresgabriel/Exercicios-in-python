nome_do_velho = ''
idade_do_velho = 0
contador = 0
media = 0
for c in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo (M) ou (F): '.upper()))
    print('-=' * 30)
    if c == 1 and sexo == 'M':
        nome_do_velho = nome
        idade_do_velho = idade
    if idade_do_velho < idade:
        idade_do_velho = idade
        nome_do_velho = nome
    if idade > 0:
        media += idade
    if sexo == 'f' and idade < 20:
        contador += 1
    if c == 1:
        nome_do_velho = nome

print(f'A média do grupo é {media / 4}')
print(f'A quantidade de mulheres com menos de 20 anos é {contador}')
print(f'O homem mais velho do grupo se chama {nome_do_velho.upper()}')
f = str(input('Digite uma frase: ')).strip().replace(' ', '')
fn = f[::-1]
print(f, fn)
if f == fn:
    print('A frase É um PALINDROMO!')
else:
    print('A frase NÃO é um PALINDROMO!')
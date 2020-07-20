notas = str(input()).split()
nota1 = float(notas[0])
nota2 = float(notas[1])
nota3 = float(notas[2])
nota4 = float(notas[3])
media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4 * 1) / 10
print('Media: {:.1f}'.format(media))
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    notaexame = float(input())
    print('Aluno em exame.')
    print('Nota do exame: {:.1f}'.format(notaexame))
    mediafinal = (media + notaexame) / 2
    if mediafinal >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(mediafinal))
    else:
        print('Aluno reprovado')
        print('Media final: {:.1f}'.format(mediafinal))
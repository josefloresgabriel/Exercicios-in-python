cont = 0
while cont < 10:
    cont = cont + 1
    nome = input('Digite o nome do paciente: ')
    idade = int(input('Digite a idade do paciente: '))
    peso = float(input('Digite o peso do paciente: '))
    altura = float(input('Digite a altura do paciente: '))
    sus = int(input('Digite o número do cartão do SUS do paciente (15 algarismos): '))
    diag = input('Digite o diagnóstico do paciente: ')
    print(f'{nome},{altura},{idade},{peso},{sus},{diag}')
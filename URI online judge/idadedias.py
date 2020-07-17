dias = int(input())
ano = dias // 365
dias -= (ano * 365)
mes = dias // 30
dias -= (mes * 30)
dia = dias / 1
print('{:.0f} ano(s)\n{:.0f} mes(es)\n{:.0f} dia(s)'.format(ano, mes, dia))

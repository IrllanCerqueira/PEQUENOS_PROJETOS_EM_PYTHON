print('--'*5,'ANALIZADOR DE NOMES','--'*5)
print()
n= 'irlan pinho cerqueira'
n= n.replace('irlan','Gostoso')
print('Seu nome em >>MAIUSCULA<< ficará: {}'.format(n.upper()))
print('Já e >>minuscula<<: {}'.format(n.lower()))
ltot= n.split()
print('{}, ao todo seu nome possui um total de: {} letras'.format(ltot[0],len(n) - n.count(' ')))
print('O seu primeiro nome é {}, e possui um tatal de {}'.format(ltot[0], len(ltot[0])))
pesquisa= input('Pesquisar palavra chave: ')
print('Existe a palavra >> {} << na variavel << {} >> ? {}!'.format(pesquisa.upper(),n.upper(), (pesquisa) in(n)))

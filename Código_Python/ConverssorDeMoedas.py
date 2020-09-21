import time
print()
time.sleep(.4)
print('-'*20)
print('<<<< CONVERSSOR DE MOEDAS >>>>')
print('-'*20)
esclh= int(input('Informe qual conversão deseja usar: \n [1] ---> [U$$ para R$] \n [2] ---> [R$ para U$$] \n OPÇÃO: '))
cot=float(input('Informe a cotação da moeda escolhida: '))
v=float(input('Informe a quantia para ser convertida: '))
if esclh == 1:
    con = v * cot
    print('O valor convertido U$$ {}, resultou em R$ {:.2f}'.format(v,con))
elif esclh == 2:
    con = v / cot
    print(' O valor convertido R$ {}, resultou em U$$ {:.2f}'.format(v,con))
else:
    print('***** OPÇÃO INVALIDA *****')
    time.sleep(.5)
    print('***** TENTE NOVAMNETE!!! *****')

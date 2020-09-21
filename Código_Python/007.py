#co= float(input('Qual o tamanho do cateto >>OPOSTO<< :'))
#ca= float(input('O comprimento do cateto >>ADJACENTE<< é: '))
#hipo= (co**2 + ca**2) ** (1/2)
#print(' O CATETO OPOSTO {}, e o cateto adjacente {}, resultaram na HIPOTENUSA {:.2f}'.format(co,ca,hipo))

from math import hypot, trunc
co= float(input('Cateto oposto é: '))
ca= float(input('Cateto adjacete: '))
hipo= hypot(ca,co)
print(trunc(hipo))
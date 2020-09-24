print('CONVERSOR DE TEMPERATURA ')
print('---'*30)
tmp= float(input('Diga a temperatura em C° :'))
Fahrenheit= tmp * 1.8 + 32
print('Sua temperatura em Celsius {}C° convertida para grau >> Fahrenheit << é: {:.1f}F°'.format(tmp,Fahrenheit))
print('---'*30) 

print('CONVERSOR DE >> Fahrenheit PAR celsius <<')
print('---'*30)
convr= float(input('Diga a  temperatura atual em  >> Fahrenheit <<: '))
cels= (convr - 32) / 1.8
print('Sua conversão de Fahrenheitde {}F° para >> celsius << resutou em: {}C°'.format(convr,cels))

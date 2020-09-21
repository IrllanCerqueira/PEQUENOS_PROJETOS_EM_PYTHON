print('><><><>< CÁLCULO DO IMC ><><><><')
print('')
alt= float(input('Digite sua altura: '))
peso= float(input('Qual seu peso atual: '))
calc=  peso / alt**2 
if calc <= 18.5:
    print(' Procure um nutricionista! \n Voçê está abaixo do peso.')
elif calc >= 18.5:
    print('Peso normal!')

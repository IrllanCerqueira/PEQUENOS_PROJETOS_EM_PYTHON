import time

while(True):
    print()
    print('><><><>< CÁLCULO DO IMC ><><><><')
    print()

    alt= float(input('Digite sua altura: '))
    peso= float(input('Qual seu peso atual: '))
    calc=  peso / (alt*alt)

    print()

    if (calc < 18.5):
        print(' IMC ATUAL: %.1f \n Procure um(a) nutricionista! \n Voçê está abaixo do peso.' %calc)
    elif (calc == 18.5)  or (calc <= 24.9):
        print(' IMC ATUAL: %.1f \n Peso normal!' %calc)
    elif(calc == 24.9) or (calc <= 30):
        print(' IMC ATUAL: %.1f \n Você está em uma categoria de SOBREPESO!' %calc)
    elif(calc > 30):
        print(' IMC ATUAL: %.1f \n NIVEIS ALTO DE OBESIDADE DETECTADO!' %calc)
        print()
        for i in range(1):
            print('AGUARDE!')
        for q in range(5):
            time.sleep(1)
            print('.'*q)
        print()
        print('PROCURE UM ESPECIALITA DE SAÚDE O MAIS BREVE POSSÍVEL!')
        print()

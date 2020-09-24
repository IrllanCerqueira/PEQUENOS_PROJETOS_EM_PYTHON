import random,time
print()
   
def descontos():
    print('____ DESCONTO DE LOJA_____')
    print()

    peca = input('Qual peça gostaria de compra? ')
    print()
    valor_aleatorio = random.randint(99, 233)
    print()
    print('A {} está no valor de R$ {}'.format(peca, valor_aleatorio))
    print()

    cupom = input('Digite seu cupom de desconto: ')
    print()
    if cupom == 'descont123':
        calculo = valor_aleatorio * 20 / 100
        aplicador_cupom = valor_aleatorio - calculo
        time.sleep(.9)
        print('APLICANDO DESCONTO EM >> {} <<'.format(peca))
        print()

        i = 0
        while i < 1:
            i += 1
            time.sleep(.8)
            print(' .. .')
            time.sleep(.8)

        print('Desconto aplicado!...')
        time.sleep(.7)
        print()
        print(' Peça: {} \n Valor: R$ {:.2f}'.format( peca, aplicador_cupom))

    else:
        print('>>>>> DESCONTO INVALIDO !!! <<<<<<')

descontos()
while (True):
    print()

    repetir = input('Deseja usar outra vez a aplicação: \n [1] >> [sim] \n [2] >> [não] \n Opção: ')
    if repetir == '1':
       descontos() 
    else:
        print('ATÈ MAIS!')
        print()

import time
print()
print('--'*23)
print('>>>>>>>>> CALCULADORA INTELIGENTE <<<<<<<<<<') 
print('--'*23)
print()
time.sleep(1.5)
n= int(input('Digite um valor númerico >> INTEIRO << : '))
print()
time.sleep(1.5)
print('Escolha operador aritmético abaixo;')
escolha= int(input(' [1] --> +\n [2] --> - \n [3] --> / \n [4] --> * \n        : '))
print('--'*23)
calq= 0
if escolha == 1:
    for x in range(11):
        calq = calq + 1
        s = calq + n
        time.sleep(.8)
        print('{} + {} = {}'.format(calq,n,s))
elif escolha == 2:
    for x in range(11):
        calq = calq + 1
        s = n - calq
        time.sleep(.8)
        print('{} - {} = {}'.format(n,calq,s))
elif escolha == 3:
    for x in range(11):
        calq= calq + 1
        s= n / calq
        time.sleep(.8)
        print('{} / {} = {:.1f}'.format(n,calq,s))
elif escolha == 4:
    for x in range(11):
        calq= calq + 1
        s= calq * n
        time.sleep(.8)
        print('{} X {} = {}'.format(calq,n,s))
else:
    time.sleep(.7)
    print('>>>>> OPÇÃO INVÁLIDA <<<<<<')
    time.sleep(.5)
    print('>>>>> TENTE NOVAMENTE <<<<<')

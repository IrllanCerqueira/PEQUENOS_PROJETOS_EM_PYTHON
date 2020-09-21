""")ATIVIDADE 01

print('Com esse programa você ira descobrir a partir de um n° o seu antecessor e o seu sucessor')
n1=int(input('Agora digite um valor númerico: '))
ant= n1 - 1
suc= n1 + 1
print('O n° digitado foi {}, e seu antecessor é {}, já o seu sucessor séra, {}!'.format(n1,ant,suc))

ATIVIDADE 02

print('Atraves de um n° descubra: \n Seu dobro? \n Seu triplo? \n E a raiz quadrada? ')
n=int(input('Diga um valor: '))
dob= n*2
tripl=n*3
raizq= n**(1/2)
print('O n° digitado foi {}, e seu dobro é {}, o triplo {}, e sua raiz quadrada {:.2f}...'.format(n,dob,tripl,raizq))

ATIVIDADE 03

print('Progrma para ler notas e calcular média do aluno')
print('')
nota1= int(input('Digite sua nota: '))
nota2= int(input('Digite sua nota: '))
result= (nota1 + nota2) / 2
print(' A nota do primeiro aluno foi {}, já a do segundo {}, loga a média dos alunos ficou em: {:.1f}'.format(nota1,ota2,result))

ATIVIDADE 04

print('Traformando >> METROS << em >> CENTIMENTROS <<')
valorM= int(input('Digite o valor em "m" a ser convertido em "cm": '))
convr= valorM * 100
print('A conersão de {}m, para "cm" resultou em {}cm'.format(valorM,convr))

ATIVIDADE 05

print('Conversor de moedas')
print('')
reais= float(input('Digite a quantia em R$ deseja converter para U$$: '))
conver= reais/5.06
print('Sua conversão de R$ {}, retornou a voçê a contia de {:.2f} U$$'.format(reais,conver))

ATIVIDADE 06

print('TABUADA DE MULTRIPLICAÇÃO')
n= int(input('Diga um n° para saber a sua tabuada: '))
tab0=n*0
tab1=n*1
tab2=n*2
tab3=n*3
tab4=n*4
tab5=n*5
tab6=n*6
tab7=n*7
tab8=n*8
tab9=n*9
tab10=n*10
print('\n {} x 0 ={}\n {} x 1 ={} \n {} x2 ={}\n {} x3 ={}\n {} x4 ={} \n {} x5 ={} \n {} x6 ={} \n {} x7 ={} \n {} x8 =} \n {} x9 ={} \n {} x10 ={}'.format(n,tab0,n,tab1,n,tab2,n,tab3,n,tab4,n,tab5,n,tab6,n,tab7,n,tab8,n,tab9,n,tab10))

#ATIVIDADE 07

print('QUANTIDADE DE TINTA A SE USAR NA PINTURA DO QUARTO')
largura= float(input('Qual a largura da parede em "m"? '))
altura= float(input('Altura da parede em "m": '))
area= altura*largura
tinta= area/2
print('Voçê presisara de {:.1f}L para pintar seu quarto!'.format(tinta))

ATIVIDADE 08

print('CÁLCULO DE DESCONTO DE LOJAS')
print('')
produto= (input('Qual produto gostaria de ver? '))
preco= float(input('Digite o valor atual do produto e ganhe 5% de_cupom na sua compra: '))
desct= preco*5
div= desct/100
desctat= preco - div
print('Voçê escolheu {}, no valor de R$ {:.2f}, e com o desconto 5% vai pagar agora R${:.2f} '.format(produto,preco,esctat))

ATIVIDADE 09

print('AUMENTO DE SALARIO')
print('')
func= input('Funcionario: ')
sat= float(input('Qual sálario recebe atualmente? '))
calculo= sat*15
aumt= calculo/100
soma= aumt + sat
print('Parabéns {}!! \n voçê acaba de ganhar um aumento de 15% no seu sálario, passando de {}, para {:.2f}'.format(func,sat,soma))"""
import random, time

print('____ DESCONTO DE LOJA_____')

peca = input('Qual peça gostaria de compra? ')
print()
valor_aleatorio = random.randint(99,233)
print()
print('A {} está no valor de R$ {}'.format(peca,valor_aleatorio))
print()

cupom = input('Digite seu cupom de desconto: ')
print()

if cupom == 'descont123':
    
    calculo= valor_aleatorio * 20 / 100
    aplicador_cupom = valor_aleatorio - calculo
    time.sleep(.9)
    print('APLICANDO DESCONTO EM >> {} <<'.format(peca))

    i=0
    while i < 1:
        i += 1 
        time.sleep(.8)
        print(' .. .')
        time.sleep(.8)
    
    print('Desconto aplicado!...')
    time.sleep(.7)
    print()
    print(' Peça: {} \n Valor: R$ {:.2f}'.format(peca,aplicador_cupom))

else:
    print()
    print('>>>>> DESCONTO INVALIDO !!! <<<<<<')


from random import choice 
n1=str(input('Digite o nome do 1° user: '))
n2=str(input('Digite o nome do 2° user: '))
n3=str(input('Digite o nome do 3° user: '))
n4=str(input('Digite o nome do 4° user: '))
lista= [n1,n2,n3,n4]
escolhido = choice(lista)
print('O escolhido entre: \n {} \n {} \n {} \n {} \n foi: {}'.format(n1,n2,n3,n4,escolhido))

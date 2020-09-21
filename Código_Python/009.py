from random import choice 
n1=str(input(''))
n2=str(input(''))
n3=str(input(''))
n4=str(input(''))
lista= [n1,n2,n3,n4]
escolhido= choice(lista)
print('O escolhido entre: {},{},{},{} foi: {} '.format(n1,n2,n3,n4,escolhido))

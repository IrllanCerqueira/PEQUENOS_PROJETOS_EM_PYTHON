from math import cos,tan,sin,radians
n= float(input('Qual o angulo: '))
c= (cos(radians(n)))
s= (sin(radians(n)))
t= (tan(radians(n)))
print(' coseno {:.2f} \n seno {:.2f} \n tangente {:.2f}\n'.format(c,s,t))
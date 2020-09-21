pizza = float(30.56)
guarana= float(25.00)
sobremesa= float(20.76)
valor1= float(pizza) * float(25) /100
valor2= float(guarana) * float(20) /100
desconto= float(valor1 + valor2 + sobremesa)
print(' Seu debito é de: R$ {:.2f}'.format(desconto))
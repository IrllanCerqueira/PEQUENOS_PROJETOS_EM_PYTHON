print('>>>>> CONERSSOR DE MEDIDAS <<<<')
n =float(input('Digite um valor númerico em Metros: '))
km = n / 1000
hm = n / 100
dam= n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('A distancia de {}M, corresponde a: \n KM: {} \n HM: {} \n DAM: {} \n DM: {} \n CM: {} \n MM: {}'.format(n,km,hm, dam, dm, cm, mm))
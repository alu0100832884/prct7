import prog1

valores = (1e1,1e2,1e3,1e4,1e5,1e6)
for valor in valores:
  y = prog1.aproximacion(valor)
  print y
  #el numero maximo de elementos de u-pla es un numero muy elevado finito
  #se producen errodes de memoria para los elementos iguales o mayores que 1e7.
  #si se pueden definir los elementus de la t-upla en notacion cientifica
  #pyc es el archibo que se crea al importar cualquier variable
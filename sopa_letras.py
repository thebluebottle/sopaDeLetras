# functions
def find(m,palabra):
      for i in m: #i = columnas, va interando columna por columna
          i = "".join(i)
          if palabra in i:
               return True
          else:
               i = 0 #si no es True reseteas i para el proximo ciclo
               for i in range(len(m)):
                    j = "".join([col[i] for col in m])
                    if palabra in j:
                         return True

# functions
def findneg(m,palabra):
      for i in m: #i = columnas, va interando columna por columna
          i = "".join(i)
          if palabra[::-1] in i:
               return True
          else:
               i = 0 #si no es True reseteas i para el proximo ciclo
               for i in range(len(m)):
                    j = "".join([col[i] for col in m])
                    if palabra[::-1] in j:
                         return True



#main----------------------------------------------------------------------------
# matriz de letras
m = [['E','L','E','F','A','N','T','E'], #ELEFANTE, JIRAFA, TORTUGA
     ['A','E','E','Z','A','Z','A','A'],
     ['Q','M','A','R','O','G','F','C'],
     ['F','U','C','E','U','R','A','N'],
     ['C','R','U','T','I','S','R','E'],
     ['C','R','R','T','I','S','I','E'],
     ['O','O','A','L','I','H','J','P'],
     ['T','S','E','N','O','T','A','R']]

palabra = input('ingresa la palabra encontrada: ').upper()
#El programa pedira palabras a encontrar hasta que el usuario ingrese ENTER(una cadena vacia)
while palabra != "":
     solucion = findneg(m,palabra)
     if solucion == True:
          print(solucion)
     else:
          solucion = find(m,palabra)
          print(solucion)
     palabra = input('ingresa la palabra encontrada: ').upper()
#print(solucion)

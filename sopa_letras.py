# functions
def find(m,palabra):
     for i in m:              #i = columnas 
          i = "".join(i)
          print(i)
          if palabra in i:
               return True



#main----------------------------------------------------------------------------
# matriz de letras
m = [['E','L','E','F','A','N','T','E'],
     ['A','E','E','Z','A','Z','A','A'],
     ['Q','M','A','R','O','S','F','C'],
     ['F','U','C','E','B','R','A','N'],
     ['C','R','U','T','I','S','R','E'],
     ['C','R','U','T','I','S','R','E'],
     ['O','W','A','L','I','H','J','P'],
     ['L','S','E','N','O','T','A','R']]

palabra = input('ingresa la palabra encontrada: ').upper()
solucion = find(m,palabra)
print(solucion)
#print(solucion)

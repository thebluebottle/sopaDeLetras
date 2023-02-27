# functions
def find(m,palabra):
     # Comprobar horizontalmente al derecho y al revez
     for fila in m:
          if palabra in ''.join(fila) or palabra in ''.join(fila[::-1]):
               print("Palabra encontrada en horizontal")
               return True

     # Comprobar verticalmente hacia arriba o hacia abajo
     for col in range(len(m[0])):
          if palabra in ''.join([fila[col] for fila in m]) or palabra in ''.join([fila[col] for fila in m][::-1]):
               print("Palabra encontrada en vertical")
               return True

     # Guarda todas las diagonales
     diags = []
     for i in range(len(m)):
          diags.append([m[i + j][j] for j in range(len(m) - i)]) # Diagonal principal hacia abajo
          diags.append([m[j][i + j] for j in range(len(m) - i)]) # Diagonal principal hacia arriba
          diags.append([m[len(m) - 1 - i - j][j] for j in range(len(m) - i)]) #Diagonal secundaria hacia arriba
          diags.append([m[len(m) - 1 - j][i + j] for j in range(len(m) - i)]) #Diagonal secundaria hacia abajo
     
     # Comprueba en todas las diagonales guardadas
     for diag in diags:
          if palabra in ''.join(diag) or palabra in ''.join(diag[::-1]):
               print("Palabra encontrada en diagonal")
               return True
     
     print("Palabra no encontrada")
     return False


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

#El programa pedira palabras a encontrar hasta que el usuario ingrese ENTER(una cadena vacia)
palabra = input('ingresa la palabra encontrada: ').upper()
while palabra != "":
     solucion = find(m,palabra)
     print(solucion)
     palabra = input('ingresa la palabra encontrada: ').upper()

# functions
def find(m,palabra):
     """ for i in m: #i = columnas, va interando columna por columna
          i = "".join(i)
          if palabra in i:
               return True
     else:
          i = 0 #si no es True reseteas i para el proximo ciclo
          for i in range(len(m)):
               j = "".join([col[i] for col in m])
               if palabra in j:
                    return True """

     n_filas = len(m)
     n_cols = len(m[0])
     for i in range(n_filas):
          for j in range(n_cols):
               if m[i][j] == palabra[0]:
                    if search(m, i, j, palabra) == True:
                         return True



def search(m, i, j, palabra):  
     founded = 1
     s_i = 1
                         
     if len(palabra) <= (len(m[i])-j): #Hay suficiente espacio para la palabra a la derecha ?
          for x in range(j+1, len(palabra)+j): #Iteramos desde esa posicion hacia la derecha en la fila
               if m[i][x] != palabra[s_i]:
                    founded = 0
                    break
               s_i += 1
     elif len(palabra) <= (j+1): #Hay espacio a la izquierda ? 
          founded = 1
          s_i = 1
          for x in range(2, j-len(palabra), -1): #Iteramos desde esa posicion hacia la izquierda en la fila
               if m[i][x] != palabra[s_i]:
                    founded = 0
                    break
               s_i += 1
     


     return founded == 1


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
     solucion = find(m,palabra)
     print(solucion)
     palabra = input('ingresa la palabra encontrada: ').upper()
print(solucion)
#print(solucion)

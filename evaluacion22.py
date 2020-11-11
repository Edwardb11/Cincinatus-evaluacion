#1
#Hacer una función recursiva que saque la suma de un numero dado y, dividirlo 
#por sí mismo. Si ingreso 5 la suma es: >>> 5+4+3+2+1 = 15 dividido en 5 = 3.


#2
#Hacer una función recursiva que lea números enteros de teclado, hasta que el 
#usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
def sumatoria():
  acomulador=0
  n=int(input("Introduzca un numero: "))
  
#3
#Hacer una función recursiva que imprima los números primos de 0 a n. 

def primos():
  inicializador=1
  Primo = int(input("Enter the number:"))
  for k in range (1, (Primo+1), 1):
    c=0
    for j in range (1, (Primo+1), 1):
      a = inicializador%j
      if (a==0):
        c = c+1
      if (c==2):
        print (inicializador)
      else:
        k = k-1

        inicializador=inicializador+1
primos()
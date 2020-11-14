#1
#Hacer una función recursiva que saque la suma de un numero dado y, dividirlo 
#por sí mismo. Si ingreso 5 la suma es: >>> 5+4+3+2+1 = 15 dividido en 5 = 3.
def suma(n):
  if n==1:
    return 1
  else:
        return n+suma(n-1)
    
def dividir(n):
    return suma(n)/n

#print(suma(5))
#print(dividir(5))    

#2
#Hacer una función recursiva que lea números enteros de teclado, hasta que el 
#usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

def sumatoria(acomulador=0):
  n=int(input("Introduzca un numero: "))
  if n!=0:
    if n>0:
      acomulador+n
      return sumatoria(acomulador+n)
  else:
    print(acomulador)
#sumatoria()

#3
#Hacer una función recursiva que imprima los números primos de 0 a n. 
#dos divisores positivos distintos: él mismo y el 1.
def esPrimo(n,cont=2):
  if (n % cont == 0 or n < 2):
    return False
  else:
    return True    

def primoList(n,x=0):
   if n == x:
      return
   if esPrimo(x):
        print(x)
   primoList(n,x + 1)

primoList(20)


#Primos sin recursividad
def Primo(n,cont=2):
  if (n % cont == 0 or n < 2):
    return False
  else:
    return True    

def Lista(n):
   primos = []
   for i in range(0,n):
      if Primo(i):
          primos.append(i)
   print(primos)
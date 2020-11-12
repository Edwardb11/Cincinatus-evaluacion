#1
#Hacer una función recursiva que saque la suma de un numero dado y, dividirlo 
#por sí mismo. Si ingreso 5 la suma es: >>> 5+4+3+2+1 = 15 dividido en 5 = 3.
def suma(n):
  if n==1:
    return 1
  else:
    return n+suma(n-1)//suma(n) #Recursion 


#print(suma(5))    
#n=int(input("Introduzca un numero: "))
#print(f"La suma del numero es {suma(n)}")
#print(f"La division de la suma numero es {suma(n/n)}")
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
def primos(n):
  losprimos=[]
  for i in range(2,n):
    if (n%i==0):
      print("")
    else:
      losprimos.append( i)
      return losprimos
n=int(input("Indroduzca el limite de numero primos: "))
print(primos(n))

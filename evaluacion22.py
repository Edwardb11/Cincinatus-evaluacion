#1
#Hacer una función recursiva que saque la suma de un numero dado y, dividirlo 
#por sí mismo. Si ingreso 5 la suma es: >>> 5+4+3+2+1 = 15 dividido en 5 = 3.
def suma(n):
  if n==1:
    return 1
  else:
    return n+suma((n-1)/n) #Recursion 


print(suma(5))    
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

def primos(numero,c):
  #inicializador=1
  #Primo = int(input("Enter the number:"))

  if numero%c==0 and numero==1:
      return False
  elif c>numero/2:
      return True
  else:
      return primos(numero,c+1)

#numero=int(input(("Digite un numero: ")))
#if primos(numero,2):
#    print("Es primo")
#else:
#      print("No")

#primos()
#primos()
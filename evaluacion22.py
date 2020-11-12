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

print(suma(5))
print(dividir(5))    

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
primos = []
 
def es_primo(numero):
    # Hacemos bucle desde 2 hasta el anterior al número
    for i in range(2, numero):
        # calculamos el resto. Si es cero => no es primo
        if numero % i == 0:
            return False
    return True
 
def calcularCantidadPrimosEnIntervalo(a, b):
    if a < 2 or b < 2:
        print ('Deben ser mayores que 1')
        return False
 
    if es_primo(a):
        primos.append(a)
 
    if a == b:
        print ('Hemos encontrado: %s primos' % len(primos))
        print (primos)
        return
 
    calcularCantidadPrimosEnIntervalo(a+1, b)
 
#calcularCantidadPrimosEnIntervalo(2, 51)
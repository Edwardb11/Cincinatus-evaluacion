#Triangulo de pascal
#agregando lista al comienzo y al final
def triangulo(n):
    lista = [[1],[1,1]]

    for i in range(1,n):
        linea = [1]
        for j in range(0,len(lista[i])-1):
            linea.extend([ lista[i][j] + lista[i][j+1] ])
        linea += [1]
        lista.append(linea)
    return lista
 
n = int(input("Numero de lineas para triangulo de Pascal: "))
print(triangulo(n))

#Utilizando el factorial para hacer el triangulo
def factorial(n):
    proceso = 1
    for i in range(n):
        proceso *= i+1
    return proceso

def nckfactorial(n, k):
	return factorial(n) / (factorial(k) * factorial(n-k))

def nckmultiplicative(n, k):
	result = 1
	for i in range(1, k+1):
		result = result * (n-(k-i))/i
	return result

def pascal(n):
	lista= []
	ns = range(n+1)
	for n in ns:
		nlist = []
		for k in range(n+1):
			nlist.append(nckmultiplicative(n, k))
		lista.append(nlist)
	return lista
n= int(input("Numero de filas : "))
print(pascal(n))

#Usando find() para reforzar mi conocimiento
def contar(cadena):
    a=0
    e=0
    ii=0
    o=0
    u=0
    for i in cadena:
        if i in "a":
            a+=1
        elif i in "e":
            e+=1
        elif i in "i":
            ii+=1
        elif i in "o":
            o+=1
        elif i in "u":
            u+=1
            
    print("A:", a)
    print("E:", e)
    print("I:", ii)
    print("O:", o)
    print("U:", u)
    return len(cadena)

cadena=input("ingrese su texto: ").lower()
print(contar(cadena))
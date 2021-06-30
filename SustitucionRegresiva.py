#Sustitucion regresiva de matriz 3x3

'''
En este caso la matriz planteada es:
[[1, -2, 4] ,             [[x1]        [[-1]
[0, 1, -2] ,               [x2]         [1]
[0, 0, 1] ]                [x3]]         [2]]
Pero cabe decir que puede colocar cualquier dato
'''
import numpy
print("\nIntroduce las dimensiones que tendra tu matriz triangular superior")
m=int(input("Introduce un numero de filas: "))
n=int(input("Introduce un numero de columnas: "))
matrix = numpy.zeros((m,n))
vector= numpy.zeros((n))
x=numpy.zeros((m))

print ("\nIntroduce los valores que tendra tu matriz")

for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=(input("Ingrese elemento a["+str(r+1)+","+str(c+1)+"]: "))
    vector[(r)]=(input('b['+str(r+1)+']: '))
print("\nMostrando matriz")
print(matrix)
print()
print(vector)

x[m-1]=vector[m-1]/matrix[m-1,n-1]
#print (x[m-1])
for r in range(m-2,-1,-1):
    suma=0
    for c in range(0,n):
        suma=suma+matrix[r,c]*x[c]
    x[r]=(vector[r]-suma)/matrix[r,r]

print ("")
print ("Resultado de la matriz propuesta: ")
print(x)
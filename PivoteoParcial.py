'''En este caso se propone como datos
[[1, -3, 2, -1] ,            [[T1] ,        [[4]
[-1, 1, 4, 3] ,              [T2],          [8]
[2, 5, 2, -1] ,               [T3];          [4]
[-2, 1, -1, 3]  ]            [T4]]          [8]]
'''

#Cabe decir que el usuario puede ingresar los datos que sea de su preferencia para la resolución del ejericico
#En mi caso yo tomare los propuestos anteriormente
#Tomar en cuenta que la matriz debe ser 4x4, dado que son 4 temperaturas
import numpy
import numpy as np
print("Introduce las dimensiones que tendra tu matriz o\n introduce la matriz planteada al inicio")
m=int(input("Introduce un numero de filas: "))
n=int(input("Introduce un numero de columnas: "))
matrix = numpy.zeros((m,n))
vector= numpy.zeros((n))
x=numpy.zeros((m))

print ("Introduce la matriz de coeficientes y el vector solución")

for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=(input("Ingrese elemento a["+str(r+1)+","+str(c+1)+"] "))
    vector[(r)]=(input('b['+str(r+1)+']: '))
print("\nLa matriz planteada es:")
print(matrix) #se imprime matriz


vector=np.transpose([vector])
print(vector)

#Matriz aumentada
matrixvector=np.concatenate((matrix,vector),axis=1)
matrixvector0=np.copy(matrixvector)
#pivoteo parcial por filas

tamano=np.shape(matrixvector)

a= tamano[0]
b=tamano[1]

for i in range(0,n-1,1):
    columna = abs(matrixvector[i : ,i])
    dondemax = np.argmax(columna)
    #intercambio de fila
    if(dondemax !=0):
        temporal = np.copy(matrixvector[i, :])
        matrixvector[i, :] = matrixvector[dondemax +i, :]
        matrixvector[dondemax +i, :]= temporal

print("\nMostrando la matriz aumentada:")
print(matrixvector0)
print("\nPivoteo parcial por filas:")
print(matrixvector)
#Eliminacion gaussiana
for k in range (0,m):
    for r in range(k+1,m):
        factor=(matrix[r,k]/matrix[k,k]) #con esta procedimiento obtenemos los ceros
        vector[r]=vector[r]-(factor*vector[k])
        for c in range(0,n):
            matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])

#sustitución regresiva
print()
x[m-1]=vector[m-1]/matrix[m-1,n-1]
#print (x[m-1])
for r in range(m-2,-1,-1):
    suma=0
    for c in range(0,n):
        suma=suma+matrix[r,c]*x[c]
    x[r]=(vector[r]-suma)/matrix[r,r]


print ("Resultado de eliminación gaussiana:")
print(matrix)
print ("")
print(vector)
print ("Resultado de la matriz propuesta: ")
print(x)
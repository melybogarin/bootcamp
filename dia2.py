

#tipo de dato integer
105
#listas
[]#lista vacia
["marce", 33, "programador"]# lista de 3 elementos 
#variables
nombre="marce"
edad=30+3
edad_mal = "30+3"
variable_lista=["hola", nombre,99]
#acceder a un elemento de la lista 
print(variable_lista[0],edad,variable_lista[2])
#Acciones /operaciones sobre listas 
variable_lista.append("rugby")#agregar elemento a la lista
variable_lista.pop()#eliminar ultimo elemento 
variable_lista[2]=50
print(variable_lista)
variable_lista[2]
print (variable_lista)

#bucles/loop/ciclos

for loquesea in variable_lista:
    print(loquesea)

# imprimir los numeros del 1 al 10
for cualquiercosa in range (10):
    print(cualquiercosa)

# imprimir el ultimo elemento de una lista sin saber cuantos 
# elementos tiene, solucion general
otra_lista=[5 ,"hola que tal","chau",4]
#solucion paso por paso 
dim_lista= len(otra_lista)
print("la dimension de otra listaes" ,dim_lista)
indice_del_ultimo = dim_lista-1
print ("el indice del ultimo elemento es ", indice_del_ultimo)
otra_lista [indice_del_ultimo]
print(otra_lista[indice_del_ultimo])
# esto es equivalente
for numero in range (1,11):
    print(numero)
# a esto 
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print(numero)

#imprimir hola 10 veces
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print("hola",numero)# imprimir numero es opcional 

###########################FUNCIONES#######################
def suma (num1, num2):
    resultado= num1+num2
    return resultado
print (suma(5,10))
resul= suma(5,8)
print (resul)

#crear una funcion resta, que reciba como parametro dos numeros 
# y retorne la resta de esos numeros
#luego llamar a la funcion e imprimir

def resta (num1,nun2):
    resultado= num1-nun2
    return resultado 
print (resta(26,23))

#crear una  funcion que reciba como parametro nombre y edad 
# e imprima "hola soy----- y tengo ---- aöos "
#llamar varias veces a la misma funcion con distintos valores 
#nota retornar es algo opcional 
def saludo (hermelinda,edad):
    print("hola soy ",hermelinda,"y tengo",edad)

saludo("willi",22)
saludo("leidy",24)
saludo("lucas",33)


#Ejercicio: Crear una funcion suma_lista que recibe como argumento  una lista de numero 
# y que retorne la suma de sus elementos 
#pista usar acumulador 
listita =[1,2,3,4,5]# 1+2+3+4+5=15

listita=[1,2,3,4,5]
a= 0
for x in listita:
    a= a+x
    print(a)

def suma_lista(listita1):
    a= 0
    for x in listita1:
        a= a+x
    return a

resul=suma_lista([100,5,5])
print(resul)# el return se guarda en resultado 

#ejercicio 2 Lista al cuadrado 
#crear una funcion que reciba una lista de numero como parametro 
# y retorne una lista con los numeros al cuadrado 
# lista_cuadrado (listita)---->[1,4,9,16,25]

def lista_cuadrada(listajeyma):
    a=[]
    for jeyma in listajeyma:
        a.append(jeyma*jeyma)
    return a
otravez=[1,4,9,16,25]
resultado_cuad = lista_cuadrada(otravez)
print(resultado_cuad)



##################################################
#ejercicio: eliminar todosw los elementos de una lista utilizando for
grupo5= ["N","f1","F2","a"]
print("antes",grupo5)
for j in range (len(grupo5)):
    grupo5.pop
print("despues",grupo5 )



#############################################33
#crear una funcion suma cuadrado que reciba una lista de numeros
# y que retorne el valor de la suma de cada numero al cuadrado 
#[1,2,3]----> 1+4+9->14

def lista_al_cuadrado(lista22):
    a=[]
    for una in lista22:
        a.append(una*una)
    return a

def suma_cuadrado(lista43):
    a=0
for x in lista43:
    a=a+x
    return a
resul= suma_cuadrado[1.2.3.4]
print(resul)



lista24=[1,2,3,4]
resultado_cuadrado= lista_al_cuadrado(lista24)
print(resultado_cuadrado)
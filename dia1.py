print(4*3)#hola suma de enteros 
print(2+2)# suma de enteros 
print(12-4)
print(12/4)
print("Hola Mundo!")#imprimir texto
print ("Exelente dia ")#Imprimir texto 
print("hola "*10)#imprimir un texto 10 veces
print("Hola Mundo" +"2")#lo siguiente es una suma/concatenacion de strings
####################################################
a = 2 # variable es el espacio donde los datos pueden modificarse constantemente 
b = 10# asignamos valor a la variable b
b = 8 #modificamos y asignamos nuevo valor de la variable 
print(a+b)#Imprimimos la suma de los valores de a y b
print(a,b)#imprime pero separa los elementos cuando usamos la , 

#Ej. Crear una variable nombre  y una variable edad 
#con sus nombres  y edades y despues imprimir 
#Hola, me llamo ------ y tengo ------a
Nombre = "hola me llamo Hermelinda "
edad = " y tengo 28 aäos "
print( Nombre ,edad)# Aasignamos valores y pynthon identifica errores de letras mayuscula y minusculas 
# eje 1 crear una variable hobby con tu pasatiempo 
# e imprimir 
# Hola me llamo ----- y tengo ---- aöos  y mi hobby es 
Nombre = "Hermelinda" 
edad = 28
Hobby = "pintar"
print ("hola, me llamo",Nombre,"y tengo ",edad,"aöos y mi hobby es",Hobby,) # se agregan las variables de acuerdo a como se presentan  
lista_vacia =[]
listax =[1,2,6,8]
print(lista_vacia)
print(listax)
datos=["MArce"]
print(datos)
alumnos= ["jose","Ramoncito",Nombre, "maria"]
print (alumnos)
# numero _alumno =3
print (alumnos[2],alumnos [0])

#Crear una lista datos que en el primer lugar este tu nombre 
#y en la segunda posicion este tu edad 
# Imprimir "hola me llamo -----, y tengo ----- aöos 
datos = ["Hermelinda", 33]
print("hola me llamo", datos[0],"y tengo", datos[1], "anhos")
datos[1]=99
print("hola me llamo", datos[0],"y tengo", datos[1], "anhos")
datos.append("programador")
print(datos)
print (datos[2])

#Ejer Agregar una profesion y un hobby a la lista de datos
# previamente creada (usar append())
# imprimir la lista 
datos.append("TRabajadora Social")
print(datos)
datos.append("pintar")
print(datos)
datos.pop() #elimina el ultimo valor agregado 
print(datos)
# funcion len()=> lenght
dimension_de_datos= len(datos)
print(dimension_de_datos)
datos.pop()
print(len(datos))
saludo = "hola que tal"
print (saludo )
print(len(saludo))

#eje. Obtener la dimension de la lista datos e imprimir: 
#"la lista datos tiene ----- elementos "
datos=["hermelinda",28]
print("la lista datos tiene", len(datos), "elementos")

#ejercicio:imprimir el ultimo elemento de una lista sin saber 
#cuantos elementos tiene , pista usar lent()
datos1=[1,5,2,7]
print (datos1)#LEN TE DA LA CANTIDAD DE ELEMENTOS ,
print(len(datos1))
print(datos1[len(datos1)-1])#LENT MENOS 1 TE DA LA POSICION DEL ELEMENTO

################### Bucles/Loops/ciclos/interacciones ###############3
lista_temas=["variables", "listas","tipos de datos"]
for concepto in lista_temas:
    print("Hoy aprendi",concepto) 
    print("que gusto!")
print("esto es lo que aprendi hoy")

for variable_for in lista_temas:
    #bloque de codigo 
    print("esto se repite ")
print ("esto no se repite")

#recorrer una lista e imprimir en cada ciclo 
#el valor del elemento con 3 signos de admiracion 
temas =["contadores!!!","psicologos!!!","trabajadores Sociales!!!"]
for concepto in temas:
    print("profesiones",concepto)
print("Fin!!!")


for x in range (10):
    print("hola",x)

# ej. imprimir los numeros del 1 al 100 usando for 
# rango 

for x in range(1,101):
    print("hola", x)

# eje2 imprimir el resultado de la suma de los numeros del 1 al 10 usando range 
suma= 0
for x in range (1,11):
    suma=suma+x
print(suma)

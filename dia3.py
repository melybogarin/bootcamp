# ing_pan = ["harina","levadura","sal","azucar"]
# def imprimir_lista(ingredientes,nombre_producto):

#     print("lista de compras de",nombre_producto)
#     print("--------------------")
#     for producto in ingredientes:
#         print(producto)



# ######################CONDICIONALES###################
# #== IGUAL 
# #>MAYOR 
# #< MENOR QUE 
# #>= MAYOR O IGUAL QUE 
# #<= MENOR O IGUAL A QUE 
# # !=DISTINTO O NO IGUAL
# a=3
# #pregunta 1
# if a > 3:
#     print("si,a es mayor a 3")
#     print("chau")
# else:
#     print("no,a no es mayor a 3")
# #pregunta 2 
# if a == 3:
#     print("a es igual a 3")

# nota= 60
# #pregunta3
# if nota>= 60:
#     print("pasasteeeee")
# else:
#     print("hule yaaaa")

# #ejercicio : crear una funcion que reciba como parametro una 
# #nota del 1 al 100 e imprima si pasaste o te aplazaste

# nota= 78
# def verificacion (puntaje):

#     if puntaje>= 78:
#         print("pasasteee")
#     else:
#         print("no pasaste")
# verificacion(nota )

# a = 11
# if a > 5 and a >10 :
#     print("a es mayor a 5 y menor que 10")
# else:
#         print("a no esta en el rango")
# if a > 5 or a < 10:
#     print("a es mayor que 5 o menor que 10")
# else:
#     print("a no es mayor que 5 ni menor que 10")

# edad = 5
# if edad > 18:
#     print("deberia estaer en la universidad")
# elif edad >13:
#     print("deberia estar en secundaria ")
# elif edad> 6:
#     print ("deberia estar en primaria ")
# else:
#     print("deberia estar en su casa")

# #anidado 
# if edad > 18:
#     print ("universidad")
# else:
#     if edad >13:
#         print("secundaria")
#     else:
#         if edad > 6:
#             print("primaria")
#         else:
#             print("bbdlc")

# # ejercicio : crear una funcion puntaje que reciba como parametro una nota 
# # del 1 al 100 e imprimir que nota sacaste
# #nota < 60 --------1
# # nota entre 60 y 70 ------2
# #nota entre 71 y 75 ----3
# #nota entre 76 y 85------4
# #nota mayor que 85------ 5


# def puntaje(nota):
#     if nota < 60:
#          print("lo siento no pasaste nota 1")
#     elif nota <=60 and nota >= 70:
#         print("pasaste apenas 2")
#     elif nota >=71 and nota <= 75:
#         print("pasaste nota 3")
#     elif nota >= 76 and nota <=85:
#         print("pasaste nota 4")
#     elif nota >= 86 and nota <=99:
#         print("pasaste nota 5")
#     puntaje (75)






# # ejercicio pedir al usuario que ingrese tres numeros y multiplicarlos
# #entre si , imprimir el resultado 
# int ("22")+ 3 #-----> 25

# num1 = int(input("ingresa el primer numero a multiplicar"))
# num2 =  int(input("ingresa el segundo numero a multiplicar"))
# num3 =  int (input("ingresa el tercer numero a multiplicar"))
# print (" el resultado es",num1*num2*num3)


# # ejercicio  2 pedir al usuario un numero del 1 al 100 y llamar a la funcion
# # que retornaba la nota que creamos hace rato 
# # utilizando el valor ingresado por el usauario 










# ########################BUCLE WHILE==MIENTRAS###################3333
# x=0
# while x != 5:
#     print ("hola esto es un bucle while ")
#     x =int (input("ingresa un numero "))
#     print ("el valor de x ahora es ", x)
# print("termino ")

# #Contador inverso 
# contador = 10
# while contador > 0:
#     print ("sigo en el bucle while")
#     contador = contador -1
#     print ("te quedan ",contador ,"oportunidades")
# print("termino")

# #Contador 
# contador = 0
# while contador < 10:
#     print("sigo en el bucle while ")
#     contador = contador + 1 
#     print ("se repitio ", contador ,"veces")

# #usando while pedir al usuario ingredientes para hacer una pizza y agregar 
# #una lista , al final imprimir la lista

# lista_ingredientes = []
# contador = 0
# while contador < 5:
#     print("hola")
#     ingre = input(" ingrese un ing:")
#     lista_ingredientes.append(ingre)
#     contador = contador + 1
# print("los ingredientes de la pizza son ", lista_ingredientes)

numero_secreto = 7
adivino = False
while adivino == False:
    apuesta =input ("ADIVINA EL NUMERO SECRETO DEL 1 AL 10:")
    if int(apuesta) == numero_secreto:
        print("gANASTE ")
        adivino = True
    else:
        print("segui participando nde arruinado")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
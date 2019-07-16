  # instanciamos y creamos el objeto robot

# # robot.move_forward()     # mueve hacia delante 
# # time.sleep(1)             # quedaa haciendo lo anterior por un segundo 
# # robot.move_left()         #hace un giro a la izquierda
# # time.sleep(0.5)         # queda haciendo el giro a la izquierda por 0.5 segundo 
# # robot.move_right()       # giro a la derecha
# # time.sleep(2)            #rueda haciendo el giro a la derecha por 2 segundos                                      
# # robot.move_backward()    # mueve el robot para atras 
# # robot.move_stop()        # pra el robot


# robot.move_forward()
# time.sleep(2)
# robot.move_right()
# time.sleep(0.5)
# robot.move_forward()
# time.sleep(2)
# robot.move_right()
# time.sleep(0.5)
# robot.move_forward()
# time.sleep(2)
# robot.move_right()
# time.sleep(0.5)
# robot.move_forward()
# time.sleep(2)
# robot.move_stop()

# for vamos  in range (1,5):
#     robot.move_forward()     #se ultiliya for que recorre de acuerdo a la cantidad 
#     time.sleep(2)
#     robot.move_left()
#     time.sleep(0.5)
# robot.move_stop()

# contador = 0
# while contador <= 3:
#     contador = contador +1
#     robot.move_forward()
#     time.sleep(2)
#     robot.move_stop()
#     robot.move_left()
#     time.sleep(0.5) 
#     robot.move_stop

#############Sensor de distancia###############3333333
# print(robot.see())
# print(robot.see() ,"centimetros")

# while True:
#     print(robot.see(),"centimetros")
#     robot.move_forward()
# obstaculo = True
# try :
#     while not obstaculo:
#         print(robot.see(),"centimetros")
#         robot.move_forward()
#         if robot.see()<= 10:
#             robot.move_stop

# except KeyboardInterrupt:
#     print("finalizado")
#     robot.move_stop()

# ejercicio utilizando un while true (bucle infinito)
#hacer que rodi avance si no encuentra un ostaculo en frente 



# try:
#     while True:
#         cm= robot.see()
#         print(cm)
#         if cm >= 10:
#             robot.move_forward()
#         else :
#             robot.move_stop()
#             robot.move_right()
#             time.sleep(0.5)
# except KeyboardInterrupt:
#     print("finalizado ")
#     robot.move_stop()


# try:
#     while True:
#         cm = robot.see() #mide la distancia 
#         print(cm)  #imprime la distancia 
#         robot.pixel(255,0,0)# muestra de color 
#         robot.pixel(100,0,0) # muestra e color 
#         robot.pixel(200,100,200) # muestra de color 
#     while cm <=20:  # mientras este a menos de 20 que avance
#         robot.move_forward# avanzamos 
#         cm= robot.see()   # volvemos a verificar que distancia estamos (es un ciclo )
#         print(cm ,"atacamos")

#     robot.mov(50,50)
# except KeyboardInterrupt:
#     print ("finalizado")
#     robot.move_stop

    
#sensor
import rodi
import time

robot = rodi.RoDI()  

# while True: 
#     print (robot.light())  # sensor de luz de rodi la cantidad de luz que detecta 
#     time.sleep(0.5)


robot.sing (800 ,10000)

####################################)
while True:
    linea = robot .sense()
    print(linea)
    print(linea[0])
    print (linea[1])
    time.sleep(0.5)
    

class Persona : #definimos la clase , un respuesta para crear un objeto
    edad = 0     # o tambien la clase es la "plantilla"# atributo o clase del objeto 

    def __init__(self,un_nombre): #__init__ es el metdodo constructor
                                   #usamos self para referirnos a un objeto de si mismo 
        self.mi_nombre = un_nombre #metodos ---- funciones dentro de la clase 
        print("hola naci,me llamo ",self.mi_nombre)
    def cumple(self):   # cumple esmetodo de la clse persona 
        self.edad = self. edad + 1 # que aumenta la propiedad edad en 1 
    def asignar_edad (self,una_edad):# asignar edad es metodo que recibe un argumento numerico 
        self.edad = una_edad    # y asigna a la propiedad edad del objeto 

    def asignar_nacionalidad (self,una_nacionalidad):
        self.nacionalidad = una_nacionalidad 
    
     
    def saludar (self):
        print( "hola soy",self.mi_nombre,"y mi nacionalidad es",self.nacionalidad)
    
pepe = Persona ("pepito")
pepe.asignar_nacionalidad ("pyo")
pepe.saludar()

# ejercicio . agregar un metodo a la clse persona que asigne una nacionalidad y otro 
# metodo que imprima "hola soy ----- y mi nacionalidad es ----""




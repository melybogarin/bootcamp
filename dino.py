
class Dino:

    ojos = 2
    def __init__(self,un_nombre,un_color,canti_patas=4,un_genero=None):
        self.nombre = un_nombre
        self.color = un_color
        self.patas = canti_patas
        self.genero = un_genero
        print("naci")
    
    def saludar(self):
        print("hola me llamo ",self.nombre,"tengo",self.patas,"patas y soy",self.color)
        
    def cortar_patas(self, cantidad_de_patas_a_cortar=1):
        self.patas = self.patas -cantidad_de_patas_a_cortar

    def decir_genero (self):
        print("hola soy",self.nombre,"y me identifico como",self.genero)


pepe=Dino("pepito","verde",4,"macho alfa pelo peludo")
print(pepe.nombre)
pepe.saludar()
pepe.decir_genero() 
pepe.cortar_patas()
pepa.genero = ("hembra")
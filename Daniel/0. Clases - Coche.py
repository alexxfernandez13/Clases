##### CLASSE vs FUNCTIONS

# - 1 logica / tematica
# - 2 para tener un objeto que lo contenga todo

class Coche():
    
    def __init__(self, marca, puertas):
        self.marca = marca
        self.puertas = puertas
        self.velocidad = 0
        
    def acelerar(self, km_h): 
        self.velocidad = self.velocidad + km_h #Porque en km_h no se pone self?
    
    def report(self):
        print(f"El coche tiem {self.puertas} puertas es de la marca {self.marca} y ahora va a velocidad {self.velocidad}")
        
    def claxon(self):
        print("MUUUUUU")
        
#instancia
coche = Coche("bmw", 4)

print(coche.velocidad) #mirando att
coche.acelerar(10) #metodo que cambia el atributo velocidad
print(coche.velocidad) #mirar velocidad

coche.report()
coche.claxon()
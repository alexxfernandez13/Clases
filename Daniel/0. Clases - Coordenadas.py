import math

class Punto():
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"
    
    def cuadrante(self):
        if self.x>=0 and self.y>=0:
            print("El punto se encuentra en el cuadrante 1")
            return 1
        elif (self.x>=0 and self.y<=0):
            print("El punto se encuentra en el cuadrante 2")
            return 2
        elif (self.x<=0 and self.y<=0):
            print("El punto se encuentra en el cuadrante 3")
            return 3
        elif (self.x<=0 and self.y>=0):
            print("El punto se encuentra en el cuadrante 4")
            return 4
        else:
            print("El punto se encuentra en el origen de coordenadas")
            return 0
    
    def vector(self,  punto): #Podria inicializarse en la misma funcion? o fuera, por ejemplo, con input
        x2 = punto.x
        y2 = punto.y
        p1 = x2-self.x
        p2 = y2-self.y
        return p1, p2
            
    def distancia(self, punto):
        x2 = punto.x
        y2 = punto.y
        dist = (x2-self.x)**2+(y2-self.y)**2
        return round(math.sqrt(dist),2)
        
punto1 = Punto(-1,-5)
punto2 = Punto (1,2)
print(punto1)
print(punto2)
######
#print(punto1.cuadrante()) -> Ejecutara funcion por tanto hara
# el print de dentro la funcion mas el print del output
cuadrante_punto1 = punto1.cuadrante() #Solo hara el print de dentro la funcion
cuadrante_punto2 = punto2.cuadrante()

#print(punto1.vector(5, 6))
print(punto1.vector(punto2))

dist= punto1.distancia(punto2) #Mejor recoger return en variable antes del print
    
print(dist)
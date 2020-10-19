# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:57:52 2020

@author: Propietario
"""
import matplotlib.pyplot as plt

class Grafico ():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def exportar_imagen(self):
        plt.plot (x,y)
        
x = [1,2,3]
y = [1,2,3]

objeto = Grafico(x, y)
objeto.exportar_imagen()


"""
PODER DE LAS CLASES VS FUNCIONES -> te da un objeto con mucha info!

xs =[[1, 2, 6], [2,3,4], [1,8,9]]
ys = [[7, 8 , 10], [2,3,4], [9,8,7]]
objetos = []
for x, y in zip(xs, ys):
    objeto = Grafico(x, y)
    objeto.exportar_imagen()
    objetos.append(objeto)
    
print(objetos)
"""


        
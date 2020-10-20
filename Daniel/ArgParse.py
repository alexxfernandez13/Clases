"""

ARGPARSE --> Codigo --> Classes

Ejercicio casa: 
    
    1) Usar funcion "argparse" para pasar dos listas de numeros (Cómo pasar una lista de numeros en argparse?? --> google)
    # lista1 = [a,b,c,d] lista2 = [1,2,3,4]
    
    if suma: 
    
    2) Hacer la suma de las dos lista de numeros
    
    if media: 
    
    3) Hacer la media de las dos listas
    
    if correlacion: 
    
    4) Hacer la correlacion entre las dos listas
    
    if plot: 
    
    4) Hacer el plot de las dos listas
    
    if diccionario: 
    
    5) Hacer un diccionario {elementolista1: elementolista2, elemento2lista2, elemento2lista2....}
    # {a:1, b:2 c:3 d:4} -> [a,b,c,d] [1,2,3,4]

"""
#como realizar ejecuciones paso a paso???

import argparse
import numpy as np
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(description='Lee, guarda y haz cosas con tu CSV!')
    parser.add_argument('-l','--list',type=list, action='append', help='Recoge 2 listas', required=True)
    parser.add_argument('--suma', action="store_true", help='Realiza la suma')
    parser.add_argument('--media', action="store_true", help='Realiza la media')
    parser.add_argument('--corr', action="store_true", help='Realiza la corr')
    parser.add_argument('--plot', action="store_true", help='Realiza el plot')
    parser.add_argument('--dicc', action="store_true", help='Realiza el dicc')
    # Use like:
    # python arg.py -l 1234 -l 2345 -l 3456 -l 4567
    args = parser.parse_args() #Lee la linea de commandline
    return args.list, args.suma, args.media, args.corr, args.plot, args.dicc
 
class Lista ():
    
    def __init__(self, lista):
        self.lista = [[int(float(j)) for j in i] for i in lista] 
        
    def output(self, suma, media, correlacion, plot, dicc):
        if suma:
            suma = [sum(x) for x in zip(*self.lista)]
            print(suma)
            
        if media:
            media = [float(sum(col))/len(col) for col in zip(*self.lista)]
            print(media)
            
        if corr:
            print(np.corrcoef(self.lista))
       
        if plot:
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.title("A test graph")
            for i in range(len(self.lista[0])):
                plt.plot([pt[i] for pt in self.lista],label = 'id %s'%i)
            plt.legend()
            plt.show()
            
        if dicc:
            print(".")

lista, suma, media, corr, plot, dicc = parse_args()

print(lista, suma, media, corr, plot, dicc)

objeto_lista = Lista (lista)

objeto_lista.output(suma, media, corr, plot, dicc)





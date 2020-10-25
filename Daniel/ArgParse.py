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

import argparse
import numpy as np
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(description='Lee, guarda y haz cosas con tu CSV!')
    "Recoger lista de listas"
    #parser.add_argument('-l1','--lista1',  type=list, action='append', help='Recoge 2 listas', required=True) 
    # Use like:
    # python arg.py -l 1234 -l 2345 -l 3456 -l 4567
    
    "Recoger lista una a una"
    parser.add_argument('-l1','--lista1',  nargs="+", type=int, help='Introduce lista1', required=True) 
    parser.add_argument('-l2','--lista2', nargs="+",  type=int, help='Introduce lista2', required=True)
    
    "Solicitar al usuario si realizar dicha accion"
    parser.add_argument('--suma', action="store_true", help='Realiza la suma')
    parser.add_argument('--media', action="store_true", help='Realiza la media')
    parser.add_argument('--corr', action="store_true", help='Realiza la corr')
    parser.add_argument('--plot', action="store_true", help='Realiza el plot')
    parser.add_argument('--dicc', action="store_true", help='Realiza el dicc')

    args = parser.parse_args() #Lee la linea de commandline
    return args.lista1, args.lista2, args.suma, args.media, args.corr, args.plot, args.dicc
 
class Lista ():
    
    def __init__(self, lista1, lista2):
        self.lista1 = lista1
        self.lista2 = lista2
        self.lista = lista1 + lista2
        
    def output(self, suma, media, corr, plot, dicc):
        if suma:
            self.suma()
            
        if media:
            self.media()
            
        if corr:
            self.correlacion()
                 
        if plot:
            self.plot()
            
        if dicc:
            self.diccionario()
            
    def suma(self):
        suma = sum(self.lista)
        print(suma)
        
    def media(self):
        media = np.mean(self.lista)
        print(media)

    def correlacion(self):
        print(np.corrcoef(self.lista))

    def plot(self):
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("A test graph")
        plt.plot(self.lista1, self.lista2)
        plt.legend()
        plt.show()
    
    def diccionario(self):
        dictionary = {}
        for elemento1, elemento2 in zip(self.lista1, self.lista2):
            dictionary[elemento1] = elemento2
        print(dictionary)

"Definir main() para la parte de las ejecuciones"
def main():
    lista1, lista2, suma, media, corr, plot, dicc = parse_args()
    print(lista1, lista2, suma, media, corr, plot, dicc)
    objeto_lista = Lista (lista1, lista2)
    objeto_lista.output(suma, media, corr, plot, dicc)

main()





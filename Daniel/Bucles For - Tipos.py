# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 13:36:50 2020

@author: Propietario
"""


#######fors######


#simple

lista1 = ["dani",2,3,4]

for elemento in lista1:
    print(elemento)
    
    
#for indice

for idx, elemento in enumerate(lista1):
    print(idx, elemento)
    
    
###for en dos listas a la vex

nombres = ["Dani", "Alejandro"]
notas = [1, 5]
for nombre, data in zip(nombres, notas):
    print(nombre, data)
    
    #hola mundo
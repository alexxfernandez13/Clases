# coding: utf-8

# # Evaluación. Análisis de datos financieros

# ## Orígenes de datos financieros
# Obtenidos a partir de la web:
#      https://www.quandl.com/api/v3/datasets/EOD/IBM.csv?api_key=yNo4hVP-pJbZzv4Amz-a

# ### Funciones de apoyo
# **a1.Función de lectura de los datos del fichero .csv**
# * Recibe como entrada el fichero.
# * Lo abre para lectura y recoge todos los valores de cierre de las acciones de la empresa.

from urllib.request import urlretrieve
import os
import statistics

def leer_datos(fichero):
    f = open(fichero, 'r') # abrir para lectura
    next(f) # saltar la linea de cabecera (es 1 línea)
    valores_cierres = []
    for linea in f: # itera línea a línea por el contenido del fichero
        valor_de_cierre = coge_cierre(linea)
        valores_cierres.append(valor_de_cierre)
    return valores_cierres

# **a2.Función para el cálculo de la media.**
# * Recibe como entrada todos los datos y devuelve el valor medio

def avg():
    pass

def calcular_metricas (long_lista):
    longitud = len(long_lista)
    media = round(statistics.mean(long_lista),2)
    maximo = max(long_lista)
    minimo = min(long_lista)
    desv_tip = round(statistics.stdev(valores_cierres_output),2)
    media_g = round(statistics.geometric_mean(valores_cierres_output),2)
    media_h = round(statistics.harmonic_mean(valores_cierres_output),2)
    mediana = round(statistics.median(valores_cierres_output),2)
    cuartil = statistics.quantiles(valores_cierres_output)
    suma = round(sum(valores_cierres_output),2)
    return longitud, media, maximo, minimo, desv_tip, media_g, media_h, mediana, cuartil, suma

# **a3.Función de transformación.**
# * Recoge una línea del csv y devuelve una lista con valores numéricos

def coge_cierre(linea):
    linea_lista = linea.split(",")
    valor_de_cierre = float(linea_lista[4])
    return valor_de_cierre

# ## PASOS 1 y 2
# ### Sentencias para descargar el fichero desde Quandl

where_the_file_is = "https://www.quandl.com/api/v3/datasets/EOD/IBM.csv?api_key=yNo4hVP-pJbZzv4Amz-a"
urlretrieve(where_the_file_is, 'datos_acciones.txt')

# ## PASO 3. Cuerpo principal del programa. 
# * Procesar el fichero línea a línea (cada línea refleja la cotización de un día)
# * Hace uso de la función de apoyo leer_datos()

valores_cierres_output = leer_datos("datos_acciones.txt") # función de lectura del .csv

# ### PASO 4.	Calcular e imprimir el mínimo, el máximo y el promedio de los valores solicitados
# * Realiza la lectura del fichero y devuelve por pantalla los valores solicitados: min, max y media.
# * Hace uso de las funciones de apoyo.

longitud, media, maximo, minimo, desv_tip, media_g, media_h, mediana, cuartil, suma = calcular_metricas(valores_cierres_output)

print("Adj_Close de la fila 0: ",valores_cierres_output[0])
print("Adj_Close de la fila 1: ",valores_cierres_output[1])
print("Número de líneas: ", longitud)
print("Máximo: ", maximo, "Mínimo: ", minimo, "Media: ", media)
print(f"Las metricas estadisticas extras añadidas son:\n-Desviacion Tipica: {desv_tip}\
\n-Media Geometrica: {media_g} \n-Media Harmonica: {media_h} \n Mediana: {mediana}\
\n-Cuartiles: {cuartil} \n-Suma: {suma}")


os.remove('datos_acciones.txt')
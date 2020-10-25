"""
classe CSV(csv):
    - Cargar los datos

    - Output(csv=False, pickle=False, parquet=False)
    
    - Media de una columna
    
    - __sum__ () --> df = datos1 + datos2
    
    CSV1 = CSV("datos1.csv")
    CSV2 = CSV("datos2.csv")
    suma = CSV1 + CSV2
    print(suma) --> datos csv1 y los datos csv2
"""
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Lee, guarda y haz cosas con tu CSV!')
    parser.add_argument('--columna', type=str, help='La columna que quieres hacer la media')
    parser.add_argument('--csv', action="store_true", help='Se guarda en CSV')
    parser.add_argument('--pickle', action="store_true", help='Se guarda en pickle')
    args = parser.parse_args() #Lee la linea de commandline
    return args.columna, args.csv, args.pickle

class CSV ():
    
    def __init__(self, df):
        self.df = pd.read_csv(df)
        
    def output(self, csv, pickle): # Input a traves de argparse -> ¿En que tipo de fichero deseas guardarlo?
        if csv:
            self.df.to_csv("output.csv")
        if pickle:
            self.df.to_pickle("output.pkl")
        # if parquet:
        #   self.df.to_parquet("output.gzip")
        else:
            print("Ningun formato especificado") #error con este else, como hacer que se refiera a todos los if?
        
    def __str__(self):
       return f"{self.df.head()}"

    def media (self, med_column):
        # media = input("Que columna quieres hacer la media?: ")
        media = self.df[med_column].mean()
        return round(media,2)
    
    def suma (self, copia):
        df_add = self.df.add(copia.df, fill_value=0)
        return df_add

columna, csv, pickle = parse_args()
print(columna, csv, pickle)
datos1 = CSV ("datos_accion.txt")
datos2 = CSV ("datos_accion.txt")

#print(datos1.df.head())
#print(datos1)
#print(datos2)

suma = datos1.suma(datos2)

print(suma)

media = datos1.media(columna)
print(media)

datos1.output(csv,pickle)
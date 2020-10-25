import pandas as pd
import numpy as np
import sklearn.preprocessing as sp
from sklearn.impute import SimpleImputer

class CSV ():
    
    """Evitar Hardcodear!!! Es decir, poner dentro de una funcion algo especifico que no se puede cambiar. 
    Pasar el elemento especifco como argumento. Interesa tener funciones generales, escalables y reutilizables"""
    
    def __init__(self, df, na_values="?",header = None, columns=None):
        self.df = pd.read_csv(df, na_values = na_values,header = header)

        if columns:
            self.df.columns = columns
        
    def __str__(self):
       return f"{self.df.head()}"

    def comprobar_faltantes (self):
        return self.df.isnull().sum()/self.df.shape[0]
    
    def mvs1 (self, columns, mode=['num-of-doors']):
        mvs = {}
        for column in columns:
            if column in mode:
                 mvs[column] = self.df[column].mode().loc[0]
            else:
                 mvs[column] = self.df[column].mean()
        
        """mvs={'normalized-losses':self.df['normalized-losses'].mean(),'num-of-doors':self.df['num-of-doors'].mode().loc[0],
             'bore':self.df['bore'].mean(),'stroke':self.df['stroke'].mean(),'horsepower':self.df['horsepower'].mean(),
             'peak-rpm':self.df['peak-rpm'].mean(),'price':self.df['price'].mean()}"""
        self.df.fillna(mvs,inplace=True)
        
    def mvs2 (self):
        #Instanciamos los imputadores de estrategia media, mediana y moda
        imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
        imp_median = SimpleImputer(missing_values=np.nan, strategy='median')
        imp_mode = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

        #Ahora rellenamos los valores faltantes de los diferentes atributos (columnas) con las diferentes estrategias
        #Para el num-of-doors sólo podemos usar la moda, pues sus valores son de tipo string
        #Para el resto usaremos la media, excepto para bore, que usaremos la mediana.
        # columns
        #for column in columns
        self.df['normalized-losses'] = imp_mean.fit_transform(self.df['normalized-losses'].values.reshape(-1,1))
        self.df['num-of-doors'] = imp_mode.fit_transform(self.df['num-of-doors'].values.reshape(-1,1))
        self.df['bore'] = imp_median.fit_transform(self.df['bore'].values.reshape(-1,1))
        self.df['stroke'] = imp_mean.fit_transform(self.df['stroke'].values.reshape(-1,1))
        self.df['horsepower'] = imp_mean.fit_transform(self.df['horsepower'].values.reshape(-1,1))
        self.df['peak-rpm'] = imp_mean.fit_transform(self.df['peak-rpm'].values.reshape(-1,1))
        self.df['price'] = imp_mean.fit_transform(self.df['price'].values.reshape(-1,1))
    
    def metricas_p1(self):
        descriptores = self.df.describe()
        #categorias_media = []
        media_categoria = self.df.groupby(["body-style","length", "width"],as_index=False).mean()
        #categorias_descriptor = []
        descriptor_atr = self.df['curb-weight'].describe()
        histograma = self.df['curb-weight'].hist();
        contar_cilindros = self.df['num-of-cylinders'].value_counts()
        moda_cilindros = self.df["num-of-cylinders"].mode()
        lista = pd.Series.sort_values(self.df['make']).unique()
        return descriptores, media_categoria, descriptor_atr, histograma, contar_cilindros, moda_cilindros, lista
   
    """
    def media_categoria(self, lista):
        media_categoria = self.df.groupby(lista, as_index=False).mean()
        
    def describe(self):
         descriptor_atr = self.df['curb-weight'].describe()
       """ 
    
    def metricas_p2(self):
        #Normalizamos con min-max
        dfminmax=self.df.copy()
        for k in self.df.columns[self.df.dtypes!=object]:
            dfminmax[k]=sp.minmax_scale(self.df[k], feature_range=(-1, 1), axis=0, copy=True)
        #Normalizamos L1
        dfL1=self.df.copy()
        for k in self.df.columns[self.df.dtypes != object]:
            dfL1[k] = sp.normalize(np.array(self.df[k]).reshape(-1, 1),norm = 'l1', axis=1, copy= True).ravel()
        #Normalizamos L2
        dfL2=self.df.copy()
        for k in self.df.columns[self.df.dtypes!=object]:
            dfL2[k]=sp.normalize(np.array(self.df[k]).reshape(1, -1),norm='l2', axis=1, copy=True).ravel()
        #Normalizamos Gauss
        dfGauss=self.df.copy()
        for k in self.df.columns[self.df.dtypes!=object]:
            dfGauss[k]=sp.scale(self.df[k], axis=0, copy=True).ravel()
        #Eliminamos las instancias que son un valor atípico para el atributo bore
        q1=self.df['bore'].quantile(0.25)
        q3=self.df['bore'].quantile(0.75)
        IQ=q3-q1
        limsup=q3+1.5*IQ
        liminf=q1-1.5*IQ
        #Observamos que en esta variable no tenemos valores atípicos, porque no hemos eliminado ninguna selección
        lim = self.df.loc[(self.df.bore>liminf)&(self.df.bore<limsup)].shape, self.df.shape
        #Creamos variables dummy para los atributos categóricos marcados en el enunciado
        dummy = pd.get_dummies(self.df,columns=['make',"fuel-system"]).head()
        return dfminmax, dfL1, dfL2, dfGauss,round(limsup,2), round(liminf,2), lim, dummy



atributos = ["symboling","normalized-losses","make","fuel-type", "aspiration",
                  "num-of-doors","body-style","drive-wheels","engine-location","wheel-base", 
                  "length","width","height","curb-weight", "engine-type","num-of-cylinders",
                  "engine-size","fuel-system", "bore","stroke","compression-ratio","horsepower", 
                  "peak-rpm","city-mpg","highway-mpg","price"]

datos1 = CSV ("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data", columns=atributos)
datos2 = CSV ("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data", columns=atributos)
datos3 = CSV ("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data", columns=atributos)

print("\n****************************PARTE 1*****************************************")
print("\n----------------------------CARGA DEL DATAFRAME-----------------------------\n",datos1)

comprobar = datos1.comprobar_faltantes()
print("\n----------------------------PROPORCION MVs----------------------------------\n",comprobar)

columnas_mvs1 = ['normalized-losses','num-of-doors','bore',"stroke",'horsepower', 'peak-rpm',"price"]
datos1.mvs1(columnas_mvs1)
print("\n----------------------------LIMPIEZA MVs------------------------------------\n",datos1)

#datos1.media_categoria([...])
#fatos1.describe[...]
#
descriptores, media_categoria, descriptor_atr, histograma, contar_cilindros, moda_cilindros, lista = datos1.metricas_p1()
print("\n----------------------------METRICAS 1--------------------------------------\n")
print(f"1. Obtén los descriptores de cada variable: \n{descriptores}\
      \n\n2. Obtén la longitud y anchuras medias por cada categoría (“body-style”): \n{media_categoria}\
      \n\n3. Analiza el atributo peso (“curb-weight”) y dibuja su histograma para apreciar si sigue alguna distribución concreta: \n{descriptor_atr}{histograma}\
      \n\n4. Analiza cuál es el número de cilindros que se da con más frecuencia en el dataset: \n{contar_cilindros},\nLa moda es: {moda_cilindros}\
      \n\n5. Obtén una lista ordenada de las diferentes marcas de coches: \n{lista}")

datos2.mvs2()
dfminmax, dfL1, dfL2, dfGauss, limsup, liminf, lim, dummy = datos2.metricas_p2()
print("\n****************************PARTE 2*****************************************")
print("\n----------------------------METRICAS 2--------------------------------------\n")
print(f"1. Vuelve a cargar el set automóviles, con valores faltantes en ciertas columnas:\n{datos3}\
      \n\n2. Introduce los valores faltantes usando la librería sklearn. Usa borrados, media, moda y mediana: \n{datos2}\
      \n\n3. Normaliza a el rango [-1,1], normaliza Gauss, normaliza L1 y L2: \n-Min/Max:\n {dfminmax}\n-Gauss:\n{dfGauss}\n-L1:\n{dfL1}\n-L2:\n{dfL2}\n\
      \n\n4. Elimina los valores que están por encima de Q1+1.5*IQ y por debajo de Q2-1.5*IQ en el atributo bore: {limsup} y {liminf}. {lim}\
      \n\n5. Transforma en variables binarias el atributo make y fuel-system: \n{dummy}")

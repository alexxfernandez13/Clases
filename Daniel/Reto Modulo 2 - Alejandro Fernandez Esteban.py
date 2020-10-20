# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:58:17 2020

@author: Propietario
"""
import pandas as pd

df = pd.read_csv("imports-85.data", na_values="?",header = None)
print(df.head())

atributos = ["symboling","normalized-losses","make","fuel-type", "aspiration";"num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
df.columns = atributos
df.head()